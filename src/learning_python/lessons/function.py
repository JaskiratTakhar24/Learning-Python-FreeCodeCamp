"""Examples of defining and calling Python functions."""


def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


def main() -> None:
    """Print a sample greeting."""
    message = greet("Python learner")
    print(message)


if __name__ == "__main__":
    main()
