#!/bin/zsh

output=$(python3 /home/labex/project/sqlite3_programming.py 2>&1)
# Check if we can query the data in users table
echo "$output" | /usr/bin/grep -q 1