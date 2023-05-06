#!/bin/zsh

if ! grep "K_UP" /home/labex/project/snake_move_snake.py;then
    exit 1
    fi

if ! grep "K_LEFT" /home/labex/project/snake_move_snake.py;then
    exit 1
    fi

if ! grep "K_RIGHT" /home/labex/project/snake_move_snake.py;then
    exit 1
    fi

grep "K_DOWN" /home/labex/project/snake_move_snake.py