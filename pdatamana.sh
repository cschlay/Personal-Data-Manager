#!/usr/bin/env bash

VENV=pdmvenv

echo "Activate the virtualenvironment."
source $VENV/bin/activate

echo "Start the server."
python3 manage.py runserver &
sleep 2
python3 -mwebbrowser http://127.0.0.1:8000