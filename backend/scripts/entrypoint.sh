#!/bin/bash

# Enter backend directory
cd $BACKEND_DIR

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Make and apply migrations:
echo "Apply database migrations"
python3 manage.py makemigrations accounts
# python3 manage.py makemigrations main_app
python3 manage.py makemigrations
python3 manage.py migrate

# Start server:
echo "Starting server"
if [ "$APP_SERVER" = "django" ]; then
    python manage.py runserver 0.0.0.0:8000
else
    gunicorn config.asgi:application --reload --bind 0.0.0.0:8000 -w 12 -k custom.uvicorn_workers.UvicornWorker --worker-tmp-dir /dev/shm
fi
