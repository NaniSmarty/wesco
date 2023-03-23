#!/bin/sh

python /home/narayanaraju/PycharmProjects/wesco/wesco_lotto/manage.py migrate --no-input
python /home/narayanaraju/PycharmProjects/wesco/wesco_lotto/manage.py collectstatic --no-input

gunicorn wesco_lotto.wsgi:application --bind 0.0.0.0:7788
