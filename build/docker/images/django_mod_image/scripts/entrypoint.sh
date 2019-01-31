#!/bin/bash


# create project
cd /opt/django
django-admin startproject helloworld

cd /opt/django/helloworld
python manage.py migrate

tail -f /dev/null
