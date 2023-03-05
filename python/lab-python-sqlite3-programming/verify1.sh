#!/bin/zsh

# Check if database file exists
if [ ! -f /home/labex/project/database.db ]; then
    echo "database.db does not exist"
    exit 1
fi