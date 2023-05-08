# Solution
```python
class MAIN:
	def __init__(self):
		self.snake = SNAKE()
		self.fruit = FRUIT()


	def update(self):
		self.snake.move_snake()
		self.check_collision()

	def check_collision(self):
		# TODO: Check collision with fruit
		if self.fruit.pos == self.snake.body[0]:
			self.fruit.randomize()
			self.snake.add_block()
		# TODO: Check collision with snake body
		for block in self.snake.body[1:]:
			if block == self.fruit.pos:
				self.fruit.randomize()
```