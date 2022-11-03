"""Test string utils"""

from __future__ import annotations

from darbia.utils.strings import random_string, split_prefix_and_number


def test_random_string() -> None:
    assert random_string(length=1, characters="a") == "a"


def test_split_prefix_and_number() -> None:
    assert split_prefix_and_number("a1") == ("a", 1)
