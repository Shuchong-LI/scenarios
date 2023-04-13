# Convert seconds to a readable format

The `time` package provides several functions to convert seconds to a readable format. One of them is the `time.ctime()` function, which converts seconds to a string representing the local time.

```python
import time

current_time = time.time()
readable_time = time.ctime(current_time)
print(readable_time)
```
