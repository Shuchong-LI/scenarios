#!/bin/zsh

# Check if the file webbrowser.py contains the key strings.

if ! grep "ArgumentParser" webbrowser.py; then
    exit 1
fi

if ! grep "parse_args" webbrowser.py; then
    exit 1
fi

if ! grep "open_new" webbrowser.py; then
    exit 1
fi

if ! grep "close" webbrowser.py; then
    exit 1
fi

if ! grep "sleep" webbrowser.py; then
    exit 1
fi

# Check if the browser is running.

ps -A | grep "firefox"
