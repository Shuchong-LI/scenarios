#!/bin/zsh

# Check if there is at least one user calles Jane Doe in the users table
if ! sqlite3 /home/labex/project/database.db "SELECT * FROM users WHERE name='Jane Doe';"; then
    echo "Jane Doe does not exist"
    exit 1
fi