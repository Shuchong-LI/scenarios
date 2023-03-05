#!/bin/zsh

# Check if example.db file exists
if ! test -f /home/labex/project/example.db; then
    echo "example.db file does not exist"
    exit 1
fi