#!/bin/zsh

# Check if database file exists
if [ ! -f /home/labex/project/example.db ]; then
    echo "database.db does not exist"
    exit 1
fi