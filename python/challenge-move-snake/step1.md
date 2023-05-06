# Move the Snake

## TODO Blocks

There are two TODO blocks in this code that need to be completed:

1. `# TODO : add new block and move the body`
2. `# TODO : move the body`

## TODO Block 1

The first TODO block involves adding a new block to the snake's body and then moving the body. To complete this, you can follow these steps:

1. Create a copy of the current body using `body_copy = self.body[:]`.
2. Insert a new block at the appropriate position using `body_copy.insert(0, body_copy[0] + self.direction)`.
3. Update the body by setting `self.body = body_copy[:]`.
4. Set `self.new_block = False` to indicate that a new block has been added.

## TODO Block 2

The second TODO block involves moving the snake's body without adding a new block. To complete this, you can follow these steps:

1. Create a copy of the current body excluding the last block using `body_copy = self.body[:-1]`.
2. Insert the new head position at the front of the copied body using `body_copy.insert(0, body_copy[0] + self.direction)`.
3. Update the body by setting `self.body = body_copy[:]`.

