#!/bin/zsh

# Check if the age of Jane Doe is updated to 40
if ! sqlite3 /home/labex/project/example.db "SELECT * FROM users WHERE name='Jane Doe' AND age=40;"; then
    echo "Jane Doe's age is not updated to 40"
    exit 1
fi