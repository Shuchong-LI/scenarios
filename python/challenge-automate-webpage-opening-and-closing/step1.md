# Automate Webpage Opening and Closing

We have already created a Python file called `webbrowser_challenge.py` on Desktop. You must use this file to write your code.

## Requirements
Your program should meet the following requirements:

1.Accept two command-line arguments:
- The URL of the webpage to open
- An optional flag to open the page in a new tab or window

2.If the flag is present, the program should open the webpage in a new tab or window, depending on the user's browser preferences. If the flag is not present, the program should open the webpage in the current tab.

## Instructions
1.Import the `webbrowser` and `argparse` modules.

2.Use the `argparse` module to parse the command-line arguments.

3.Store the command-line arguments in variables.

4.Use the `webbrowser` module to open the specified URL in a new tab or window, depending on the user's preference.

5.Handle any errors that might occur.

## Example

To run the program, save the code to the given file `webbrowser_challenge.py`, open a command prompt or terminal window in the directory where the file is saved, and enter a command similar to the following:

```bash
python /home/labex/Desktop/webbrowser_challenge.py https://www.google.com --new-window
```

This should open Google's homepage in a new window. If you omit the `--new-window` flag, the page will open in the current tab.

You can customize the program to open any webpage by modifying the command-line arguments. 
