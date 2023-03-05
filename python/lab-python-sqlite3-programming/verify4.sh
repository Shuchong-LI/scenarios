#!/bin/zsh

# Check if we can query the data in users table
if ! sqlite3 /home/labex/project/database.db "SELECT * FROM users;"; then
    echo "users table is empty"
    exit 1
fi