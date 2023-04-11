# Automate Webpage Opening and Closing

## Requirements

Your program should meet the following requirements:

1. Accept three command-line arguments:
   - The URL of the webpage to open
   - The number of seconds to wait before closing the browser
   - An optional flag to open the page in a new tab or window
2. If the flag is present, the program should open the webpage in a new tab or window, depending on the user's browser preferences. If the flag is not present, the program should open the webpage in the current tab.
3. After opening the webpage, the program should wait for the specified number of seconds before closing the browser.
4. If any errors occur during the process, the program should print an error message.

## Instructions

1. Import the `webbrowser` and `time` modules.
2. Use the `argparse` module to parse the command-line arguments.
3. Store the command-line arguments in variables.
4. Use the `webbrowser` module to open Google homepage(https://www.google.com) in a new tab or window.
5. Use the `time` module to wait for the specified number of seconds.
6. Use the `webbrowser` module to close the browser.
   
## Example

To run the program, save the code to a file named `webbrowser_challenge.py`, open a command prompt or terminal window in the directory where the file is saved, and enter a command similar to the following:

```
python webbrowser_challenge.py https://www.google.com 10 --new-window
```

This should open Google's homepage in a new window and close the browser after 10 seconds. If you omit the `--new-window` flag, the page will open in the current tab.

You can customize the program to open any webpage and wait for any number of seconds before closing the browser by modifying the command-line arguments. This program can be useful in situations where you need to automate the process of opening a webpage and performing some action, such as downloading a file or filling out a form.
