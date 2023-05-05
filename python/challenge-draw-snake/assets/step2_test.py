import unittest
import pygame
from pygame.math import Vector2
from snake_draw_snake import SNAKE

import sys
sys.path.append("/home/labex/project")


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

    def test_update_head_graphics(self):
        self.snake.body = [Vector2(0, 0), Vector2(1, 0), Vector2(2, 0)]
        self.snake.update_head_graphics()
        self.assertEqual(self.snake.head, self.snake.head_left)

        self.snake.body = [Vector2(0, 0), Vector2(-1, 0),Vector2 (-2, 0)]
        self.snake.update_head_graphics()
        self.assertEqual(self.snake.head, self.snake.head_right)

        self.snake.body = [Vector2(0, 0), Vector2(0, 1), Vector2(0, 2)]
        self.snake.update_head_graphics()
        self.assertEqual(self.snake.head, self.snake.head_up)

        self.snake.body = [Vector2(0, 0), Vector2(0, -1),Vector2 (0, -2)]
        self.snake.update_head_graphics()
        self.assertEqual(self.snake.head, self.snake.head_down)

    def test_update_tail_graphics(self):
        self.snake.body = [Vector2(0, 0), Vector2(1, 0), Vector2(2, 0)]
        self.snake.update_tail_graphics()
        self.assertEqual(self.snake.tail, self.snake.tail_right)

        self.snake.body = [Vector2(0, 0), Vector2(-1, 0),Vector2 (-2, 0)]
        self.snake.update_tail_graphics()
        self.assertEqual(self.snake.tail, self.snake.tail_left)

        self.snake.body = [Vector2(0, 0), Vector2(0, 1), Vector2(0, 2)]
        self.snake.update_tail_graphics()
        self.assertEqual(self.snake.tail, self.snake.tail_down)

        self.snake.body = [Vector2(0, 0), Vector2(0, -1),Vector2 (0, -2)]
        self.snake.update_tail_graphics()
        self.assertEqual(self.snake.tail, self.snake.tail_up)

if __name__ == '__main__':
    unittest.main()
