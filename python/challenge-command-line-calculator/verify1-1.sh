#!/bin/zsh

if ! python3 /home/labex/project/calculator.py;
then
    exit 1
fi

if ! grep "argparse.ArgumentParser" /home/labex/project/calculator.py;
then
    exit 1
fi

grep "description" /home/labex/project/calculator.py;