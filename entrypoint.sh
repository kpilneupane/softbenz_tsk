#!/bin/sh

set -e

echo "Waiting for 5 seconds before starting..."
sleep 5

mkdir -p /app/data

# remove database if it doesnot exist or missing migrations
if [ ! -f /app/data/db.sqlite3 ] || [ ! -d /app/app/migrations ]; then
    echo "Creating fresh database..."
    rm -f /app/data/db.sqlite3
    
    mkdir -p /app/app/migrations
    touch /app/app/migrations/__init__.py
    
    # Removing old migrations
    find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
    find . -path "*/migrations/*.pyc" -delete
    
    # Creating new database
    touch /app/data/db.sqlite3
    chmod 777 /app/data/db.sqlite3
    
    echo "Making fresh migrations..."
    python manage.py makemigrations app
fi

echo "Running migrations..."
python manage.py migrate

echo "Loading initial data..."
python manage.py loaddata full_database.json || echo "No data.json found, skipping initial data load..."


echo "Starting Django server....."
exec "$@"