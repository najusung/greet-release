"""Print a greeting from the command line."""

import sys


def greet(name: str, punctuation: str = "!") -> str:
    """Return a greeting for name, using world when name is blank."""
    if not name.strip():
        name = "world"
    return f"Hello, {name}{punctuation}"


def main() -> int:
    """Greet the first command-line argument, or world when it is missing."""
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(name))
    return 0


def test_greet() -> None:
    assert greet("Hee") == "Hello, Hee!"


def test_greet_blank() -> None:
    assert greet(" ") == "Hello, world!"


def test_greet_punctuation() -> None:
    assert greet("Hee", ".") == "Hello, Hee."


if __name__ == "__main__":
    raise SystemExit(main())
