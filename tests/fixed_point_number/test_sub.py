import pytest

from fixed_point_number import FixedPointNumber, sub


def test_FixedPointNumber_sub_000():
    x = FixedPointNumber(100, 100)
    y = FixedPointNumber(100, 100)
    z = sub(x, y)
    assert z.internal == 0
    assert z.scale == 100


def test_FixedPointNumber_sub_100():
    x = FixedPointNumber(100, 100)
    y = 1
    with pytest.raises(Exception) as e:
        _ = sub(x, y)
    assert str(e.value) == "value must be a FixedPointNumber."


def test_FixedPointNumber_sub_101():
    x = FixedPointNumber(100, 100)
    y = FixedPointNumber(100, 10)
    with pytest.raises(Exception) as e:
        _ = sub(x, y)
    assert str(e.value) == "The scale factor is differ: 100 and 10."
