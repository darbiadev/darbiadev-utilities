"""Test string utils"""

from __future__ import annotations

from darbia.utils.strings import (
    bulk_substring_remove,
    find_nth,
    random_string,
    split_prefix_and_number,
)


def test_random_string() -> None:
    assert random_string(length=1, characters="a") == "a"


def test_split_prefix_and_number() -> None:
    assert split_prefix_and_number("a1") == ("a", 1)


def test_find_nth() -> None:
    assert find_nth("here's johnny", "o", 1) == 8
    assert find_nth("orale ya vamos", "a", 3) == 10


def test_bulk_substring_remove() -> None:
    assert bulk_substring_remove("here's johnny", ["he", "joh"]) == "re's nny"
    assert bulk_substring_remove("orale ya vamos", ["ya", "am"]) == "orale  vos"
