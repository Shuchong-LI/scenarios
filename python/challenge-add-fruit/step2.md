# Add the Fruit Class

## 1. Code Introduction

This code defines the `FRUIT` class for a snake game implemented using the Pygame library in Python. The `FRUIT` class has two methods, `draw_fruit()` and `randomize()`.

The `draw_fruit()` method is responsible for drawing the fruit object on the game screen. It uses the `pygame.Rect()` function to create a rectangular object with the position and size of the fruit object, and then draws the fruit image using `screen.blit()` function.

The `randomize()` method is responsible for randomly selecting a position for the fruit object on the game screen. It uses the `random.randint()` function to generate two random integers between 0 and `cell_number - 1`, which are used to determine the x and y coordinates of the fruit object. The position of the fruit object is stored as a `Vector2` object.

## 2. TODO Blocks

There are two `TODO` blocks in the code. Here are the instructions for each one:

### TODO: Draw fruit

The `draw_fruit()` method has a `TODO` block which instructs to draw the fruit. To do this, we need to add code that will actually draw the fruit image on the game screen. We can do this by first creating a `pygame.Rect` object with the position and size of the fruit object. Then, we can use the `screen.blit()` function to draw the fruit image on the game screen.

### TODO: Randomize fruit position

The `randomize()` method has a `TODO` block which instructs to randomize the fruit position. To do this, we need to generate two random integers between 0 and `cell_number - 1` by using the `random.randint()` function. These integers will be used to determine the x and y coordinates of the fruit object. We can then create a `Vector2` object with these coordinates and store it as the position of the fruit object.
