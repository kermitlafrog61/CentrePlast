#!/bin/sh

until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 2
done

python manage.py collectstatic --noinput

# gunicorn core.wsgi --bind 0.0.0.0:8000 --workers 3 --threads 3
python manage.py runserver 0.0.0.0:8000