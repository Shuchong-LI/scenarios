# Draw the Score
This code is a method called `draw_score` in a Snake game developed using the Pygame library. The purpose of this method is to draw the current score on the screen for the player to see during gameplay. The score is determined by the length of the snake's body (minus the initial three segments) when it eats an apple. 

## TODOs

- `# TODO: draw score` - this comment suggests that the code is incomplete and that we need to write code to draw the score on the screen. The following lines of code are used to create various elements required to draw the score:
    1. `score_text = None` - this line should calculate the current score by subtracting the initial length of the snake from its current length and converting it to a string.
    2. `score_surface = None` - this line should create a Pygame surface object that contains the score text and is used to display it on the screen. 
    3. `score_x` and `score_y` - these variables determine the position of the score surface on the screen.
    4. `score_rect = None` - this line should create a rectangle object around the score surface and centers it at the position specified by `score_x` and `score_y`.
    5. `apple_rect` - this variable creates a rectangle object around the apple image.
    6. `bg_rect` - this variable creates a rectangle object that serves as the background for the score and the apple.


## Requirements

- To complete the `score_text` variable, use the `len()` function to calculate the length of the snake's body and subtract 3 from it.Then, convert the result to a string using the `str()` function.
- To complete the `score_surface` variable, use the `game_font.render()` function to create a surface object that contains the score text.
- To complete the `score_rect` variable, use the `score_surface.get_rect()` function to create a rectangle object around the score surface and center it at the position specified by `score_x` and `score_y`.
- To complete the `apple_rect` variable, use the `apple.get_rect()` function to create a rectangle object around the apple image and place it to the left of the score rectangle.
- To complete the `bg_rect` variable, use the `pygame.Rect()` function to create a rectangle object that combines the apple rectangle and the score rectangle.
- Use the `pygame.draw.rect()` function to draw a rectangle around the score and the apple.
- Use the `screen.blit()` function to draw the score and the apple on the screen.
