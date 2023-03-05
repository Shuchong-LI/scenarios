#!/bin/zsh

# Check if we can query the data in users table
sqlite3 /home/labex/project/example.db "SELECT * FROM users;" | grep -q 1