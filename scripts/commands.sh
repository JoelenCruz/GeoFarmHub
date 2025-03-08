#!/bin/sh

# mkdir -p /data/web/media/avatars
# cp -r /djangoapp/static/images/avatars/* /data/web/media/avatars/

# The shell will terminate script execution when a command fails
set -e

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST $POSTGRES_PORT) ..."
  sleep 2
done

echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"

python manage.py collectstatic --noinput
python manage.py makemigrations core --noinput
python manage.py migrate --noinput
# python manage.py runserver_plus --print-sql 0.0.0.0:8000
python manage.py runserver 0.0.0.0:8000