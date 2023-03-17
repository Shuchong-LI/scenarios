#!/bin/zsh

cat ~/.zsh_history | grep -q "mv mytextfile.txt"

cd /home/labex/Desktop/challenge3

my_file="mytextfile.txt"
for file in *; do
    if ! diff -q "$my_file" "$file" > /dev/null; then
        exit 1
    fi
done
