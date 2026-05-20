import pytest

from claims_analysis.transformations import add_numbers


@pytest.mark.parametrize(
    "a,b,expected,exception",
    [
        (1, 2, 3, None),
        (3, 3, 6, None),
        (3, "A", None, TypeError),
    ],
)
def test_add_numbers(a, b, expected, exception):
    if exception is None:
        assert add_numbers(a, b) == expected
    else:
        with pytest.raises(exception):
            add_numbers(a, b)


# @timing_decorator
# def some_long_fcn():
#     print("bla")
