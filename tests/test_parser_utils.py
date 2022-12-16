"""Test parser utils"""

from __future__ import annotations

import pytest

from darbia.utils.parsers import range_parser


@pytest.mark.parametrize(
    "value,result",
    [
        ("5 - 8", [5, 6, 7, 8]),
        ("5, 7, 10", [5, 7, 10]),
        ("5, 7-10", [5, 7, 8, 9, 10]),
    ],
)
def test_range_parser(value: str, result: list[int]):
    assert range_parser(value) == result
