# Convert a time object to a string

You can convert a time object to a string using the `time.strftime()` function. This function takes a format string as an argument and returns a string representing the time object.

```python
import time

date_string = "2022-03-01 14:30:00"
format_string = "%Y-%m-%d %H:%M:%S"
time_object = time.strptime(date_string, format_string)

new_format_string = "%B %d, %Y %H:%M:%S"
new_date_string = time.strftime(new_format_string, time_object)

print(new_date_string)
```
