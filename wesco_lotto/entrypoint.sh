#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn wesco_lotto.wsgi:application --bind 0.0.0.0:7788