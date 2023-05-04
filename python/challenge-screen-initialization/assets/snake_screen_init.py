import pygame,sys,random

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
cell_size = None # TODO:Choose your cell size.
cell_number = None # TODO:Choose your cell number.
screen = None # TODO: Choose your screen size.
clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == SCREEN_UPDATE:
			pass


	screen.fill(('''R''','''G''','''B'''))# TODO:Choose your favorite RGB color.
	pygame.display.update()
	clock.tick(60)

	