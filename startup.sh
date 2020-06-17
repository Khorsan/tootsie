#!/bin/bash
ping -c 2 db 

# exit 2

./manage.py check && \
    ./manage.py makemigrations && \
    ./manage.py migrate && \
    ./manage.py migrate && \
    ./manage.py createsuperuser && \
    ./manage.py runserver
