#!/bin/zsh

# Check if the table users exists in example.db
if ! sqlite3 /home/labex/project/example.db "SELECT name FROM sqlite_master WHERE type='table' AND name='users';"; then
    echo "users table does not exist"
    exit 1
fi