# Load Images and Initialize the Snake's Body

We have created the python file `snake_draw_snake.py` in `/home/labex/project` for you.This code defines a class called `SNAKE` which is responsible for loading images of the snake in various positions and initializing the snake's body.

## TODO blocks:

* TODO: Load the snake graphics: Here you need to load the images of the snake in various positions. The images are located in the 'Graphics' folder and have names such as `head_up.png`, `head_down.png`, `tail_up.png`, etc. Use the `pygame.image.load()` function to load each image and store them in variables such as `self.head_up`.
* TODO: Initialize the snake body: Here you need to initialize the snake's body by creating a list of `Vector2` objects. Each `Vector2` object represents a segment of the snake's body. The `Vector2` objects should be initialized with the following values: `Vector2(5,10)`, `Vector2(4,10)`, `Vector2(3,10)`. The `Vector2` objects are stored in a list called `self.body`.

## Requirements:

- You need to use `convert_alpha()` method to optimize the images for drawing.
- The body of the snake should be continuous, i.e., there should be no gaps between the body segments.
