import unittest
import pygame

import sys
sys.path.append("/home/labex/project")

from snake_draw_snake import SNAKE

class TestSnake(unittest.TestCase):
    def setUp(self):
        pygame.mixer.pre_init(44100,-16,2,512)
        pygame.init()
        cell_size = 40
        cell_number = 20
        pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))

        self.snake = SNAKE()

    def tearDown(self):
        pygame.quit()

    def test_init(self):
        self.assertEqual(len(self.snake.body), 3)
        self.assertEqual(self.snake.body[0], pygame.math.Vector2(5, 10))
        self.assertEqual(self.snake.body[1], pygame.math.Vector2(4, 10))
        self.assertEqual(self.snake.body[2], pygame.math.Vector2(3, 10))

        self.assertIsInstance(self.snake.head_up, pygame.Surface)
        self.assertIsInstance(self.snake.head_down, pygame.Surface)
        self.assertIsInstance(self.snake.head_right, pygame.Surface)
        self.assertIsInstance(self.snake.head_left, pygame.Surface)
        self.assertIsInstance(self.snake.tail_up, pygame.Surface)
        self.assertIsInstance(self.snake.tail_down, pygame.Surface)
        self.assertIsInstance(self.snake.tail_right, pygame.Surface)
        self.assertIsInstance(self.snake.tail_left, pygame.Surface)
        self.assertIsInstance(self.snake.body_vertical, pygame.Surface)
        self.assertIsInstance(self.snake.body_horizontal, pygame.Surface)
        self.assertIsInstance(self.snake.body_tr, pygame.Surface)
        self.assertIsInstance(self.snake.body_tl, pygame.Surface)
        self.assertIsInstance(self.snake.body_br, pygame.Surface)
        self.assertIsInstance(self.snake.body_bl, pygame.Surface)

if __name__ == '__main__':
    unittest.main()
