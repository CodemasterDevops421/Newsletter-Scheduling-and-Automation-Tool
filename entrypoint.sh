#!/bin/bash

echo "Applying migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
gunicorn --workers 3 --bind 0.0.0.0:8000 newsletter_tool.wsgi:application
