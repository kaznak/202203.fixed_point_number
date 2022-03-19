import pytest

from fixed_point_number import FixedPointNumber


def test_FixedPointNumber_add_000():
    x = FixedPointNumber(100, 100)
    y = FixedPointNumber(100, 100)
    z = x.add(y)
    assert z.internal == 200
    assert z.scale == 100


def test_FixedPointNumber_add_100():
    x = FixedPointNumber(100, 100)
    y = 1
    with pytest.raises(Exception) as e:
        _ = x.add(y)
    assert str(e.value) == "value must be a FixedPointNumber."


def test_FixedPointNumber_add_101():
    x = FixedPointNumber(100, 100)
    y = FixedPointNumber(100, 10)
    with pytest.raises(Exception) as e:
        _ = x.add(y)
    assert str(e.value) == "The scale factor is differ between 100 and 10."
