# Solution

```python
	def check_fail(self):
		# TODO: check if snake is outside of screen
		if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
			self.game_over()
		# TODO: check if snake hits itself
		for block in self.snake.body[1:]:
			if block == self.snake.body[0]:
				self.game_over()
		
	def game_over(self):
		# TODO: reset game
		self.snake.reset()
```