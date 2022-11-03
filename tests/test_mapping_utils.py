"""Test mapping utils"""

from __future__ import annotations

from darbia.utils.mappings import dict_compare


def test_dict_compare() -> None:
    old_dict = {"a": 1, "b": 2, "d": 7}
    new_dict = {"b": 3, "c": 4, "d": 7}
    comparison_results = (["c"], ["a"], {"b": (2, 3)}, ["d"])
    assert dict_compare(old_dict=old_dict, new_dict=new_dict) == comparison_results
