#!/bin/bash -ex

# Move into the backend directory
cd $BACKEND_DIR

# Load all media files
cp fixtures/to_media/* media-serve/

# Load `auth` app fixtures in correct order
python manage.py loaddata fixtures/auth/group.json

# Load `accounts` app fixtures in correct order
python manage.py loaddata fixtures/accounts/customuser.json

# Load `main_app` app fixtures in correct order
# ... To be added ...
