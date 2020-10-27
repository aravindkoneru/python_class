import week1_tues
import pytest


@pytest.mark.parametrize("text,sanitized", [
    ("original", "original"),
    ("  OrIgInAL   ", "original"),
    ("SoMe DIRTY STRING     ", "some dirty string"),
    ("   asdfrew  fdsarWWWW", "asdfrew  fdsarwwww" )
])
def test_sanitize1(text, sanitized):
    result = week1_tues.sanitize1(text)
    desired = f"original: {text}, sanitized: {sanitized}"

    assert result == desired

@pytest.mark.parametrize("text,sanitized", [
    ("original", "\nORIGINAL\t"),
    ("    strip left", "\n    STRIP LEFT\t"),
    ("sTRiP RIGHT     \n", "\nSTRIP RIGHT\t"),
])
def test_sanitized2(text, sanitized):
    result = week1_tues.sanitize2(text)
    desired = f"sanitized: {sanitized}"

    assert result == desired


@pytest.mark.parametrize("x,xs", [
    (1, 1),
    (12, 144),
    (3, 9),
    (16, 256)
])
def test_numbers1(x, xs):
    assert week1_tues.numbers1(x) == xs
