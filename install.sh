#!/usr/bin/env bash

VENV=pdmvenv

echo "Create a virtual environment for Python 3."
python3 -m venv $VENV

echo "Activate the virtualenvironment."
source $VENV/bin/activate
pip3 install -r requirements.txt
