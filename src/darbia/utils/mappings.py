"""Assorted utility functions."""

from collections import defaultdict
from typing import Any, TypeVar

T = TypeVar("T")


def dict_compare(
    old_dict: dict[Any, Any],
    new_dict: dict[Any, Any],
) -> tuple[list[Any], list[Any], dict[Any, Any], list[Any]]:
    """
    Compare two different dictionaries.

    Parameters
    ----------
    old_dict : dict[Any, Any]
        The old dictionary
    new_dict : dict[Any, Any]
        The new dictionary

    Returns
    -------
    Comparison results : (list[Any], list[Any], dict[Any, Any], list[Any])

    Examples
    --------
    >>> dict_compare(old_dict=dict(), new_dict=dict())
    ([], [], {}, [])

    Notes
    -----
    https://stackoverflow.com/a/18860653
    """
    old_dict_keys: set[Any] = set(old_dict.keys())
    new_dict_keys: set[Any] = set(new_dict.keys())
    intersecting_keys: set[Any] = old_dict_keys.intersection(new_dict_keys)
    new_keys: set[Any] = new_dict_keys - old_dict_keys
    removed_keys: set[Any] = old_dict_keys - new_dict_keys
    modified_keys: dict[Any, tuple[Any, Any]] = {
        key: (old_dict[key], new_dict[key]) for key in intersecting_keys if old_dict[key] != new_dict[key]
    }
    unmodified_keys: set[Any] = {o for o in intersecting_keys if old_dict[o] == new_dict[o]}
    return list(new_keys), list(removed_keys), modified_keys, list(unmodified_keys)


def get_nested_dict_value(
    dct: dict,
    keypath: str,
    default: T = None,
    separator: str = ".",
) -> T:
    """
    Parse nested values from dictionaries.

    Parameters
    ----------
    dct
        The dictionary to search
    keypath
        The path of keys to check through
    default
        The default value to return if the value is not found
    separator
        The character used to split the keypath

    Returns
    -------
    The value at the keypath or the default value

    Examples
    --------
    >>> get_nested_dict_value({"key": {"path": "value"}}, "key.path")
    'value'
    """
    keys = keypath.split(separator)

    value = dct
    for key in keys:
        value = value.get(key)

        if not value:
            value = default
            break

    return value


def keychain(dicts: list[dict]) -> dict:
    """
    Create a dict of chains of keys from sequential dicts.

    Parameters
    ----------
    dicts
        The list of dictionaries to chain

    Returns
    -------
    A dictionary of lists of all chains

    Notes
    -----
    https://discord.com/channels/267624335836053506/587375768556797982/1044549320948584528
    """
    output = defaultdict(list)

    first, *dicts = dicts
    for key, value in first.items():
        output[key].append(value)

    for dct in dicts:
        for key, value in output.items():
            last_value = value[-1]
            # pylint: disable-next=unnecessary-dict-index-lookup
            output[key].append(dct[last_value])

    return output
