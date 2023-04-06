#!/bin/zsh

if ! python3 /home/labex/project/calculator.py;
then
    exit 1
fi

if ! grep -e "add_argument('-a'" -e "add_argument('--add'" /home/labex/project/calculator.py;
then
    exit 1
fi

if ! grep -e "add_argument('-s'" -e "add_argument('--subtract'" /home/labex/project/calculator.py;
then
    exit 1
fi

if ! grep -e "add_argument('-m'" -e "add_argument('--multiply'" /home/labex/project/calculator.py;
then
    exit 1
fi

if ! grep -e "add_argument('-d'" -e "add_argument('--divide'" /home/labex/project/calculator.py;
then
    exit 1
fi