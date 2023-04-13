# Parse a string to a time object

You can parse a string representing a date and time to a time object using the `time.strptime()` function. This function takes a string and a format string as arguments and returns a time object.

```python
import time

date_string = "2022-03-01 14:30:00"
format_string = "%Y-%m-%d %H:%M:%S"
time_object = time.strptime(date_string, format_string)

print(time_object)
```