# Solution
```python
# calculator.py
import argparse

def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b

def subtract(a: int, b: int) -> int:
    """Return the difference of two numbers."""
    return a - b

def multiply(a: int, b: int) -> int:
    """Return the product of two numbers."""
    return a * b

def divide(a: int, b: int) -> float:
    """Return the quotient of two numbers."""
    return a / b

if __name__ == '__main__':
    # TODO: Creat a parser and a group.
    parser = argparse.ArgumentParser(description='Perform arithmetic operations on two numbers.')
    group = parser.add_mutually_exclusive_group()

    # TODO: Add and parse the arguments.
    group.add_argument('-a', '--add', nargs=2, type=int, metavar=('NUM1', 'NUM2'), help='add NUM1 and NUM2')
    group.add_argument('-s', '--subtract', nargs=2, type=int, metavar=('NUM1', 'NUM2'), help='subtract NUM2 from NUM1')
    group.add_argument('-m', '--multiply', nargs=2, type=int, metavar=('NUM1', 'NUM2'), help='multiply NUM1 and NUM2')
    group.add_argument('-d', '--divide', nargs=2, type=int, metavar=('NUM1', 'NUM2'), help='divide NUM1 by NUM2')
    args = parser.parse_args()

    # TODO: Output management.
    if args.add:
        result = add(*args.add)
        print(f"{args.add[0]} + {args.add[1]} = {result}")
    elif args.subtract:
        result = subtract(*args.subtract)
        print(f"{args.subtract[0]} - {args.subtract[1]} = {result}")
    elif args.multiply:
        result = multiply(*args.multiply)
        print(f"{args.multiply[0]} * {args.multiply[1]} = {result}")
    elif args.divide:
        result = divide(*args.divide)
        print(f"{args.divide[0]} / {args.divide[1]} = {result}")
    else:
        parser.print_help()
```