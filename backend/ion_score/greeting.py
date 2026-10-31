"""Example of a pure core: receives values, returns a value, never touches the terminal."""

DEFAULT_NAME = "monde"


def build_greeting(name: str) -> str:
    return f"Bonjour, {name.strip() or DEFAULT_NAME} !"
