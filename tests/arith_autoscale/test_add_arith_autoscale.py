import pytest

from fixed_point_number import FixedPointNumber
from fixed_point_number.arith_autoscale import add


def test_FixedPointNumber_add_000():
    x = FixedPointNumber(100, 100)
    y = FixedPointNumber(100, 100)
    z = add(x, y)
    assert z.internal == 200
    assert z.scale == 100


def test_FixedPointNumber_add_102():
    x = FixedPointNumber(100, 100)
    y = FixedPointNumber(100, 10)
    z = add(x, y)
    assert z.internal == 1100
    assert z.scale == 100


def test_FixedPointNumber_add_100():
    x = FixedPointNumber(100, 100)
    y = 1
    with pytest.raises(Exception) as e:
        _ = add(x, y)
    assert str(e.value) == "value must be a FixedPointNumber."
