## Game Over

This is a part of the code for a Snake Game. The `check_fail` function is responsible for detecting if the game is over, and it does so in two ways. First, it checks if the snake's head is outside of the game screen. Second, it checks if the snake's head has collided with its body.

If either of these conditions is true, the `game_over` function is called, which resets the game by calling the `reset` method of the `Snake` object.

## TODO Blocks

1. `TODO: check if snake is outside of screen` - This block of code checks whether the snake's head is outside the game screen. To accomplish this, the x and y coordinates of the snake's head are compared to the size of the game screen. If either coordinate is outside the range of 0 to the size of the game screen (which is represented by the `cell_number` variable), then the `game_over` function is called. You could add an additional feature that displays a message when the snake hits the border or prevents the snake from crossing the border altogether.

2. `TODO: check if snake hits itself` - This block of code checks if the snake's head has collided with its own body. It does so by looping through each block of the snake's body (excluding the head) and checking if any of them are in the same position as the head. If a collision is detected, the `game_over` function is called. You could add an additional feature that displays a message when the snake hits itself.

3. `TODO: reset game` - This block of code is called when the game is over, and it is responsible for resetting the game. It does so by calling the `reset` method of the `Snake` object. You could add additional features to this method, such as updating the high score or displaying a message when the game is over.
