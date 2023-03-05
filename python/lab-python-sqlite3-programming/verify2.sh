#!/bin/zsh

# Check if the users table exists in database.db
if ! sqlite3 /home/labex/project/database.db "SELECT name FROM sqlite_master WHERE type='table' AND name='users';"; then
    echo "users table does not exist"
    exit 1
fi