# Solution

```python
	def draw_score(self):
		# TODO: draw score
		score_text = str(len(self.snake.body) - 3)
		score_surface = game_font.render(score_text,True,(56,74,12))
		score_x = int(cell_size * cell_number - 60)
		score_y = int(cell_size * cell_number - 40)
		score_rect = score_surface.get_rect(center = (score_x,score_y))
		apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))
		## The background rectangle is created by combining the apple rectangle and the score rectangle
		bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6,apple_rect.height)

		## draw background rectangle
		pygame.draw.rect(screen,(167,209,61),bg_rect)

		## draw score and apple
		screen.blit(score_surface,score_rect)
		screen.blit(apple,apple_rect)
		
		## draw rectangle around score and apple
		pygame.draw.rect(screen,(56,74,12),bg_rect,2)
```