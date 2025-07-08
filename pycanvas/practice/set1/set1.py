def is_even(n: int) -> bool | None:
    """Return True if the number is even, False otherwise."""
    return n % 2 == 0  # Check if the number is even # Add your code here


def average(numbers: list[float]) -> float | None:
    """
    Return the average of a list of numbers.
    If the list is empty, raise a ValueError.
    """
    if not numbers:
        raise ValueError("The list cannot be empty.")
    return sum(numbers) / len(numbers)  # Calculate the average of the numbers


def is_positive(n: int) -> bool | None:
    """Return True if the number is positive, False otherwise"""
    return n > 0
