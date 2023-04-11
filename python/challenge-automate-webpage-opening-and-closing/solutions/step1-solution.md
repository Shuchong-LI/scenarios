# Solution

```python
import webbrowser
import time
import argparse

parser = argparse.ArgumentParser(description='Open a web page and close the browser after a specified amount of time.')
parser.add_argument('url', help='the URL of the webpage to open')
parser.add_argument('wait_time', type=int, help='the number of seconds to wait before closing the browser')
parser.add_argument('--new-window', action='store_true', help='open the webpage in a new window')

args = parser.parse_args()

url = args.url
wait_time = args.wait_time
new_window = args.new_window

try:
    if new_window:
        webbrowser.open_new(url)
    else:
        webbrowser.open(url)
    time.sleep(wait_time)
    webbrowser.close()
except Exception as e:
    print("An error occurred:", e)
```
