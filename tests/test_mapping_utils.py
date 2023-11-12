"""Test mapping utils."""

from __future__ import annotations

from darbia.utils.mappings import dict_compare, get_nested_dict_value, keychain


def test_dict_compare() -> None:
    old_dict = {"a": 1, "b": 2, "d": 7}
    new_dict = {"b": 3, "c": 4, "d": 7}
    comparison_results = (["c"], ["a"], {"b": (2, 3)}, ["d"])
    assert dict_compare(old_dict=old_dict, new_dict=new_dict) == comparison_results


def test_get_nested_dict_value() -> None:
    data = {"key": {"path": "value"}}
    result_value = get_nested_dict_value(data, "key.path")
    assert result_value == "value"
    result_none = get_nested_dict_value(data, "key.other")
    assert result_none is None


def test_keychain() -> None:
    dicts = [
        {"a": "b", "v": "w", "o": "p"},
        {"b": "c", "w": "x", "p": "q"},
        {"c": "d", "x": "y", "q": "r"},
    ]

    new_dict = {"a": ["b", "c", "d"], "v": ["w", "x", "y"], "o": ["p", "q", "r"]}

    assert keychain(dicts) == new_dict
