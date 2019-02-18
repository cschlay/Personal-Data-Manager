#!/usr/bin/env bash

VENV=pdmvenv

echo "Activate the virtualenvironment."
source $VENV/bin/activate

echo "Start the server."
python3 manage.py runserver