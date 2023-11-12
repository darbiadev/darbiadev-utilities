"""Test iterable utils."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from darbia.utils.iterables import chunks, enumerate2, flatten

if TYPE_CHECKING:
    from collections.abc import Iterable


@pytest.mark.parametrize(
    ("iterable", "start", "step", "output"),
    [
        ("abc", 0, 1, [(0, "a"), (1, "b"), (2, "c")]),
        ("abc", 1, 2, [(1, "a"), (3, "b"), (5, "c")]),
        ("abc", 2, 3, [(2, "a"), (5, "b"), (8, "c")]),
        ("abc", 0, -1, [(0, "a"), (-1, "b"), (-2, "c")]),
        ("abc", -1, -2, [(-1, "a"), (-3, "b"), (-5, "c")]),
    ],
)
def test_enumerate2(iterable: Iterable, start: int, step: int, output: Iterable) -> None:
    assert list(enumerate2(iterable, start, step)) == output


def test_chunks() -> None:
    lst = [1, 2, 3, 4, 5, 6]
    assert list(chunks(lst, 3)) == [(1, 2, 3), (4, 5, 6)]


def test_flatten() -> None:
    assert flatten([["a"], ["b"], ["c"]]) == [
        "a",
        "b",
        "c",
    ]
