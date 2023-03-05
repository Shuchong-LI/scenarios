#!/bin/zsh

# Check if the user Jane Doe is deleted from the users table
if ! sqlite3 /home/labex/project/database.db "SELECT * FROM users WHERE name='Jane Doe';"; then
    echo "Jane Doe is not deleted"
    exit 1
fi