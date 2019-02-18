#!/usr/bin/env bash

VENV=pdmvenv

echo "Create a virtual environment for Python 3."
python3 -m venv $VENV

echo "Activate the virtualenvironment."
source $VENV/bin/activate
pip3 install -r requirements.txt

echo "Initialize the tables."
python3 manage.py makemigrations budget dashboard cli library recipes
python3 manage.py migrate

echo "Create yourself a superuser."
python3 manage.py createsuperuser

echo "Start the server."
python3 manage.py runserver