# Solution

```python
def move_snake(self):
    if self.new_block == True:
        # TODO : add new block and move the body
        body_copy = self.body[:]
        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy[:]
        self.new_block = False
    else:
        # TODO : move the body
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy[:]
```