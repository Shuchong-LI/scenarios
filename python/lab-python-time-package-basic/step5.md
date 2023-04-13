# Measure the execution time of a code block

You can measure the execution time of a code block using the `time.perf_counter()` function. This function returns the current value of a performance counter, which is used to measure the time elapsed between two points in time.

```python
import time

start_time = time.perf_counter()

# Code block to measure
for i in range(1000000):
    pass

end_time = time.perf_counter()

print("Execution time:", end_time - start_time, "seconds")
```
