import json
from typing import Optional


def process_data(data: list) -> list:
    """Double all non-None values in a list."""
    return [item * 2 for item in data if item is not None]


def save_file(data: list, filename: str) -> None:
    """Save data to a JSON file safely."""
    try:
        with open(filename, 'w') as f:
            json.dump(data, f)
    except OSError as e:
        raise OSError(f"Failed to save file: {e}")


def load_file(filename: str) -> list:
    """Load data from a JSON file safely."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except OSError as e:
        raise OSError(f"Failed to load file: {e}")


def calculate(a: float, b: float, operation: str) -> Optional[float]:
    """Perform basic arithmetic with error handling."""
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'divide':
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    return None
