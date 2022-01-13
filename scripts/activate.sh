#!/bin/bash

python3 -m venv ./env

source ./env/bin/activate

pip3 install --upgrade pip

pip3 install -r ./requirements.txt

pip3 install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.0.0-py3-none-any.whl