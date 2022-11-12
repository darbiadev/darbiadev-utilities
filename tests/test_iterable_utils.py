"""Test iterable utils"""

from __future__ import annotations

from darbia.utils.iterables import chunks, enumerate2, flatten


def test_enumerate2() -> None:
    assert list(enumerate2("abc", 0, 1)) == [(0, "a"), (1, "b"), (2, "c")]
    assert list(enumerate2("abc", 1, 2)) == [(1, "a"), (3, "b"), (5, "c")]
    assert list(enumerate2("abc", 2, 3)) == [(2, "a"), (5, "b"), (8, "c")]
    assert list(enumerate2("abc", 0, -1)) == [(0, "a"), (-1, "b"), (-2, "c")]
    assert list(enumerate2("abc", -1, -2)) == [(-1, "a"), (-3, "b"), (-5, "c")]


def test_chunks() -> None:
    lst = [1, 2, 3, 4, 5, 6]
    assert list(chunks(lst, 3)) == [(1, 2, 3), (4, 5, 6)]


def test_flatten() -> None:
    assert flatten([["a"], ["b"], ["c"]]) == [
        "a",
        "b",
        "c",
    ]
