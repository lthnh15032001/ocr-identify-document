#!bin/bash

echo $OSTYPE

if [[ $OSTYPE == "Win32" ]]; then 
    echo "Oh no! Win32 unsupport."
else
    python3 -m venv ./env

    source env/bin/activate

    pip3 install -r ./requirements.txt
fi
