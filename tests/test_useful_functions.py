"""Testing the utilities module"""

from darbia.util import (
    chunks,
    dict_compare,
    enumerate2,
    flatten,
    random_string,
    split_prefix_and_number,
)


def test_dict_compare() -> None:
    old_dict = {"a": 1, "b": 2, "d": 7}
    new_dict = {"b": 3, "c": 4, "d": 7}
    comparison_results = (["c"], ["a"], {"b": (2, 3)}, ["d"])
    assert dict_compare(old_dict=old_dict, new_dict=new_dict) == comparison_results


def test_enumerate2() -> None:
    assert list(enumerate2("abc", 0, 1)) == [(0, "a"), (1, "b"), (2, "c")]
    assert list(enumerate2("abc", 1, 2)) == [(1, "a"), (3, "b"), (5, "c")]
    assert list(enumerate2("abc", 2, 3)) == [(2, "a"), (5, "b"), (8, "c")]
    assert list(enumerate2("abc", 0, -1)) == [(0, "a"), (-1, "b"), (-2, "c")]
    assert list(enumerate2("abc", -1, -2)) == [(-1, "a"), (-3, "b"), (-5, "c")]


def test_chunks() -> None:
    lst = [1, 2, 3, 4, 5, 6]
    assert list(chunks(lst, 3)) == [[1, 2, 3], [4, 5, 6]]


def test_flatten() -> None:
    assert flatten([["a"], ["b"], ["c"]]) == [
        "a",
        "b",
        "c",
    ]


def test_random_string() -> None:
    assert random_string(length=1, characters="a") == "a"


def test_split_prefix_and_number() -> None:
    assert split_prefix_and_number("a1") == ("a", 1)
