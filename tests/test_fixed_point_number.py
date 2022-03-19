import pytest

from fixed_point_number import __version__, FixedPointNumber


def test_version():
    assert __version__ == "0.1.0"


def test_FixedPointNumber_constructor_000():
    x = FixedPointNumber(100, 100)
    assert x.internal == 100
    assert x.scale == 100


def test_FixedPointNumber_constructor_100():
    with pytest.raises(Exception) as e:
        _ = FixedPointNumber(100, 0)
    assert str(e.value) == "scaling factor must be a positive integer."


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


def test_FixedPointNumber_sub_000():
    x = FixedPointNumber(100, 100)
    y = FixedPointNumber(100, 100)
    z = x.sub(y)
    assert z.internal == 0
    assert z.scale == 100


def test_FixedPointNumber_sub_100():
    x = FixedPointNumber(100, 100)
    y = 1
    with pytest.raises(Exception) as e:
        _ = x.sub(y)
    assert str(e.value) == "value must be a FixedPointNumber."


def test_FixedPointNumber_sub_101():
    x = FixedPointNumber(100, 100)
    y = FixedPointNumber(100, 10)
    with pytest.raises(Exception) as e:
        _ = x.sub(y)
    assert str(e.value) == "The scale factor is differ between 100 and 10."
