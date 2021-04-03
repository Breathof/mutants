#!/bin/bash

DATABASE=./adn.db

# Create database
if [[ ! -e "$DATABASE" ]]; then
    python3 data_base_init.py || python data_base_init.py
fi

pip3 -r requirements.txt || pip -r requirements.txt

python3 ./src/main.py || python ./src/main.py