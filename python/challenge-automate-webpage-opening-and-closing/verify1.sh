#!/bin/zsh

# Check if the file webbrowser.py contains the key strings.

if ! grep -q "ArgumentParser" webbrowser.py; then
    exit 1
fi

if ! grep -q "parse_args" webbrowser.py; then
    exit 1
fi

if ! grep -q "open_new" webbrowser.py; then
    exit 1
fi

if ! grep -q "close" webbrowser.py; then
    exit 1
fi

if ! grep -q "sleep" webbrowser.py; then
    exit 1
fi

# Check if the browser is running.

pgrep -x "net"
