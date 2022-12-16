"""Assorted utility functions"""

from __future__ import annotations


def range_parser(text: str) -> list[int]:
    """
    Parse the numbers in text

    Parameters
    ----------
    text
        The text to parse

    Returns
    -------
    The list of numbers in the parsed ranges

    Examples
    --------
    >>> range_parser("1,2-5")
    [1, 2, 3, 4, 5]

    Notes
    -----
    https://discord.com/channels/267624335836053506/267624335836053506/1047647967143792661
    """
    output = []
    text = text.replace(" ", "")
    items = text.split(",")
    for item in items:
        if "-" in item:
            start, stop = item.split("-")
            output.extend(list(range(int(start), int(stop) + 1)))
        else:
            output.append(int(item))
    return output
