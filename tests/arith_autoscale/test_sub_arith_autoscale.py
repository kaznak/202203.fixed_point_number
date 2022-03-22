import pytest

from fixed_point_number import FixedPointNumber
from fixed_point_number.arith_autoscale import sub


def test_FixedPointNumber_sub_000():
    x = FixedPointNumber(100, 100)
    y = FixedPointNumber(100, 100)
    z = sub(x, y)
    assert z.internal == 0
    assert z.scale == 100


def test_FixedPointNumber_sub_001():
    x = FixedPointNumber(100, 100)
    y = FixedPointNumber(100, 10)
    z = sub(x, y)
    assert z.internal == -900
    assert z.scale == 100


def test_FixedPointNumber_sub_100():
    x = FixedPointNumber(100, 100)
    y = 1
    with pytest.raises(Exception) as e:
        _ = sub(x, y)
    assert str(e.value) == "value must be a FixedPointNumber."
