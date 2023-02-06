#!/bin/sh

# enxit immediately if there is any error in one of the scripts/commands
set -e

python manage.py collectstatic --noinput

gunicorn --bind 0.0.0.0:8000 langpal.wsgi:application
