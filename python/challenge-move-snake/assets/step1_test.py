import unittest
import pygame
from snake_move_snake import SNAKE
from pygame.math import Vector2


class TestSnake(unittest.TestCase):
    def setUp(self):
        pygame.mixer.pre_init(44100,-16,2,512)
        pygame.init()
        cell_size = 40
        cell_number = 20
        pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))

        self.snake = SNAKE()
        self.snake.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        

    def tearDown(self):
        pygame.quit()

    def test_move_snake(self):
        self.snake.direction = (0, -1)
        self.snake.new_block = False
        self.snake.move_snake()
        self.assertEqual(self.snake.body, [Vector2(5,9),Vector2(5,10),Vector2(4,10)])
        self.snake.direction = (1, 0)
        self.snake.new_block = True
        self.snake.move_snake()
        self.assertEqual(self.snake.body, [Vector2(6,9),Vector2(5,9),Vector2(5,10),Vector2(4,10)])
if __name__ == '__main__':
    unittest.main()
