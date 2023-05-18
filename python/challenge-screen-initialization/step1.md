# Screen Initialization

The files are placed in the `/home/labex/project` directory.

## TODO blocks

1. `cell_size = None` - Choose a cell size. This variable represents the size of each cell in the grid that will be displayed on the screen.
2. `cell_number = None` - Choose the number of cells. This variable represents the number of cells that will be displayed on the screen.
3. `screen = None` - Choose the screen size. This variable represents the size of the game window that will be displayed on the screen.
4. `screen.fill(('''R''','''G''','''B'''))` - Choose your favorite RGB color. This line of code fills the screen with a color determined by the RGB values that are passed as arguments.

## Requirements

- The type of the `cell_size` variable should be `int`.
- The type of the `cell_number` variable should be `int`.
- You `screen` variable should use the `pygame.display.set_mode()` method to create a game window with the specified size.
- The RGB values passed to the `screen.fill()` method should be integers between 0 and 255. 