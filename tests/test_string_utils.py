"""Test string utils."""

from __future__ import annotations

import json
from datetime import timedelta

import pytest
from darbia.utils.strings import (
    CustomEncoder,
    bulk_substring_remove,
    find_nth,
    random_string,
    split_prefix_and_number,
)


def test_random_string() -> None:
    assert random_string(length=1, characters="a") == "a"


@pytest.mark.parametrize(
    ("text", "output"),
    [
        ("a1", ("a", 1)),
        ("a1000", ("a", 1000)),
        ("x1", ("x", 1)),
    ],
)
def test_split_prefix_and_number(text: str, output: tuple[str, int]) -> None:
    assert split_prefix_and_number(text) == output


def test_custom_encoder() -> None:
    assert json.dumps(timedelta(seconds=15), cls=CustomEncoder) == '"0:00:15"'


@pytest.mark.parametrize(
    ("text", "char", "nth", "index"),
    [
        ("here's johnny", "o", 1, 8),
        ("orale ya vamos", "a", 3, 10),
    ],
)
def test_find_nth(text: str, char: str, nth: int, index: int) -> None:
    assert find_nth(text, char, nth) == index


@pytest.mark.parametrize(
    ("text", "strings", "output"),
    [
        ("here's johnny", ["he", "joh"], "re's nny"),
        ("orale ya vamos", ["ya", "am"], "orale  vos"),
    ],
)
def test_bulk_substring_remove(text: str, strings: list[str], output: str) -> None:
    assert bulk_substring_remove(text, strings) == output
