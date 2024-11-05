#!/bin/bash

python3 -m venv tux_env

pip3 install --upgrade pip

source tux_env/bin/activate

pip3 install -r requirements.txt
