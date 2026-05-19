
from claims_analysis.transformations import add_nums

import pytest


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (0, 0, 0),
        (-1, 1, 0),
        (100, 200, 300),
    ]
)
def test_add_numbers(a, b, expected):
    result = add_nums(a, b)
    assert result == expected, f"Expected {expected} but got {result}"


def test_if_add_num_breaks_on_str():
    with pytest.raises(TypeError):
        add_nums("2", "3")
