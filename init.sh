#!/bin/bash

DATABASE=./adn.db
DEPENDENCIES="flask requests waitress pytest-cov"

# Create database
if [[ ! -e "$DATABASE" ]]; then
    python3 data_base_init.py || python data_base_init.py
fi

pip3 install $DEPENDENCIES || pip install $DEPENDENCIES

python3 ./src/main.py || python ./src/main.py