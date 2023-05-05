import pygame,sys,random
from pygame.math import Vector2

class SNAKE:
	def __init__(self):
		# TODO: Load the snake graphics.
		self.head_up = None
		self.head_down = None
		self.head_right = None
		self.head_left = None
		
		self.tail_up = None
		self.tail_down = None
		self.tail_right = None
		self.tail_left = None

		self.body_vertical = None
		self.body_horizontal = None

		self.body_tr = None
		self.body_tl = None
		self.body_br = None
		self.body_bl = None

		# TODO:Initialize the snake body.
		self.body = None

	def update_head_graphics(self):
		# TODO: Update the snake head graphics.
		head_relation = self.body[1] - self.body[0]

	def update_tail_graphics(self):
		# TODO: Update the snake tail graphics.
		tail_relation = self.body[-2] - self.body[-1]

	def draw_snake(self):
		self.update_head_graphics()
		self.update_tail_graphics()

		for index,block in enumerate(self.body):
			# TODO: Define the x and y position of the block.
			x_pos = None 
			y_pos = None

			block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

			if index == 0:
				# TODO: Draw the snake head.
			elif index == len(self.body) - 1:
				# TODO: Draw the snake tail.
			else:
				previous_block = self.body[index + 1] - block
				next_block = self.body[index - 1] - block
				if previous_block.x == next_block.x:
					# TODO: Draw the snake body.
				elif previous_block.y == next_block.y:
					# TODO: Draw the snake body.
				else:
					if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
						# TODO: Draw the snake body.
					elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
						# TODO: Draw the snake body.
					elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
						# TODO: Draw the snake body.
					elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
						# TODO: Draw the snake body bottom right.


if __name__ == "__main__":
	pygame.mixer.pre_init(44100,-16,2,512)
	pygame.init()
	cell_size = 40
	cell_number = 20
	screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
	clock = pygame.time.Clock()

	SCREEN_UPDATE = pygame.USEREVENT
	pygame.time.set_timer(SCREEN_UPDATE,150)

	snake = SNAKE()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == SCREEN_UPDATE:
				pass


		screen.fill((175,215,70))#RGB color
		snake.draw_snake()
		pygame.display.update()
		clock.tick(60)

	