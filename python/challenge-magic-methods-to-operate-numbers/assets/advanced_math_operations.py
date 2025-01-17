class MathExpression:
    def __init__(self, value: int):
        """Initializes the class with an integer value.

        Args:
            value (int): An integer used to initialize the class
        """
        self.value = value

    def __pow__(self, other: "MathExpression") -> "MathExpression":
        """Raises one instance of the class to the power of another.
        Args:
            other (MathExpression): The other MathExpression object to pow
        Returns:
            MathExpression: A new MathExpression object containing the computed result
        """

        # TODO

        return

    def __mod__(self, other: "MathExpression") -> "MathExpression":
        """Returns the modulo of one instance of the class by another.
        Args:
            other (MathExpression): The other MathExpression object to mod
        Returns:
            MathExpression: A new MathExpression object containing the computed result
        """

        # TODO

        return

    def __floordiv__(self, other: "MathExpression") -> "MathExpression":
        """Returns the floor division of one instance of the class by another.
        Args:
            other (MathExpression): The other MathExpression object to floordiv
        Returns:
            MathExpression: A new MathExpression object containing the computed result
        """

        # TODO

        return

    def __str__(self) -> str:
        """Returns a string representation of the value of the instance.

        Returns:
            str: Stringify the object
        """
        return str(self.value)
