def greet(name: str) -> str:
    return f"Hello, {name}!"


def main() -> None:
    message = greet("Python learner")
    print(message)


if __name__ == "__main__":
    main()
