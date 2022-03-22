import pytest

from fixed_point_number import FixedPointNumber


def test_FixedPointNumber_constructor_000():
    x = FixedPointNumber(100, 100)
    assert x.internal == 100
    assert x.scale == 100


def test_FixedPointNumber_constructor_100():
    with pytest.raises(Exception) as e:
        _ = FixedPointNumber(100, 0)
    assert str(e.value) == "scaling factor must be a positive integer."
