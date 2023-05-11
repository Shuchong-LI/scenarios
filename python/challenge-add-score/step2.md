# Draw the Score
This code is a method called `draw_score` in a Snake game developed using the Pygame library. The purpose of this method is to draw the current score on the screen for the player to see during gameplay. The score is determined by the length of the snake's body (minus the initial three segments) when it eats an apple. 

## TODOs

- `# TODO: draw score` - this comment suggests that the code is incomplete and that we need to write code to draw the score on the screen. The following lines of code are used to create various elements required to draw the score:
    1. `score_text = str(len(self.snake.body) - 3)` - this line calculates the current score by subtracting the initial length of the snake from its current length and converting it to a string.
    2. `score_surface = game_font.render(score_text,True,(56,74,12))` - this line creates a Pygame surface object that contains the score text and is used to display it on the screen. 
    3. `score_x` and `score_y` - these variables determine the position of the score surface on the screen.
    4. `score_rect = score_surface.get_rect(center = (score_x,score_y))` - this line creates a rectangle object around the score surface and centers it at the position specified by `score_x` and `score_y`.
    5. `apple_rect` - this variable creates a rectangle object around the apple image.
    6. `bg_rect` - this variable creates a rectangle object that serves as the background for the score and the apple.

- Each of the above TODOs requires the implementation of the code mentioned in the comments. For example, to draw the score on the screen, we need to use the `screen.blit()` method to display the score surface at the position specified by `score_rect`.
