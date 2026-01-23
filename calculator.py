"""
Calculator Module
Provides basic mathematical operations
"""
from typing import Union

Number = Union[int, float]


class Calculator:
    """A simple calculator class with basic arithmetic operations."""

    def __init__(self):
        """Initialize the calculator with operation history."""
        self.history = []

    def add(self, a: Number, b: Number) -> Number:
        """
        Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b
        """
        result = a + b
        self._record_operation("add", a, b, result)
        return result

    def subtract(self, a: Number, b: Number) -> Number:
        """
        Subtract b from a.

        Args:
            a: First number
            b: Second number

        Returns:
            Difference of a and b
        """
        result = a - b
        self._record_operation("subtract", a, b, result)
        return result

    def multiply(self, a: Number, b: Number) -> Number:
        """
        Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b
        """
        result = a * b
        self._record_operation("multiply", a, b, result)
        return result

    def divide(self, a: Number, b: Number) -> Number:
        """
        Divide a by b.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            Quotient of a divided by b

        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a / b
        self._record_operation("divide", a, b, result)
        return result

    def power(self, base: Number, exponent: Number) -> Number:
        """
        Calculate base raised to the power of exponent.

        Args:
            base: The base number
            exponent: The power to raise to

        Returns:
            base raised to the power of exponent
        """
        result = base ** exponent
        self._record_operation("power", base, exponent, result)
        return result

    def _record_operation(self, operation: str, a: Number, b: Number, result: Number) -> None:
        """Record an operation to history."""
        self.history.append({
            "operation": operation,
            "operands": (a, b),
            "result": result
        })

    def get_history(self) -> list:
        """Return the operation history."""
        return self.history.copy()

    def clear_history(self) -> None:
        """Clear the operation history."""
        self.history = []


# Example usage:
if __name__ == "__main__":
    calculator = Calculator()
    print(calculator.add(5, 3))  # Output: 8
    print(calculator.subtract(10, 4))  # Output: 6
    print(calculator.multiply(7, 2))  # Output: 14
    print(calculator.divide(9, 3))  # Output: 3.0
    print(calculator.power(2, 3))  # Output: 8
    print(calculator.get_history())  # Output: [{'operation': 'add', 'operands': (5, 3), 'result': 8}, {'operation': 'subtract', 'operands': (10, 4), 'result': 6}, {'operation': 'multiply', 'operands': (7, 2), 'result': 14}, {'operation': 'divide', 'operands': (9, 3), 'result': 3.0}, {'operation': 'power', 'operands': (2, 3), 'result': 8}]
    calculator.clear_history()
    print(calculator.get_history())  # Output: []