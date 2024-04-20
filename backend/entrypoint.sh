# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Make and apply migrations:
echo "Apply database migrations"
python3 manage.py makemigrations
python3 manage.py migrate

# Start server:
echo "Starting server"
if [ "$DEPLOYMENT_STAGE" = "DEVELOPMENT" ]; then
    python manage.py runserver 0.0.0.0:8000
else
    gunicorn config.asgi:application --reload --bind 0.0.0.0:8000 -w 12 -k custom.uvicorn_workers.UvicornWorker
fi
