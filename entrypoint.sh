#!/bin/sh

set -e

echo "Running migrations..."
python manage.py migrate

echo "Loading initial data..."
python manage.py loaddata full_database.json || echo "No data.json found, skipping initial data load..."

# Start the application
exec "$@"
