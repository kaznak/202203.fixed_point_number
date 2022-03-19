import pytest

from fixed_point_number import FixedPointNumber

from logging import WARNING, getLogger

logger = getLogger(__name__)


def test_FixedPointNumber_div_000():
    x = FixedPointNumber(100, 100)
    y = FixedPointNumber(100, 100)
    z = x.div(y)
    assert z.internal == 100
    assert z.scale == 100


def test_FixedPointNumber_div_001(caplog):
    caplog.set_level(WARNING)
    x = FixedPointNumber(10000, 100)
    y = FixedPointNumber(300, 100)
    z = x.div(y)
    assert z.internal == 3333
    assert z.scale == 100
    assert caplog.record_tuples == [
        ("fixed_point_number.fixed_point_number", WARNING, "drop surplus: 0.01")
    ]


def test_FixedPointNumber_div_002(caplog):
    caplog.set_level(WARNING)
    x = FixedPointNumber(10000, 100)
    y = FixedPointNumber(-300, 100)
    z = x.div(y)
    assert z.internal == -3334
    assert z.scale == 100
    assert caplog.record_tuples == [
        ("fixed_point_number.fixed_point_number", WARNING, "drop surplus: -0.02")
    ]


def test_FixedPointNumber_div_100():
    x = FixedPointNumber(100, 100)
    y = 1
    with pytest.raises(Exception) as e:
        _ = x.div(y)
    assert str(e.value) == "value must be a FixedPointNumber."


def test_FixedPointNumber_div_101():
    x = FixedPointNumber(100, 100)
    y = FixedPointNumber(100, 10)
    with pytest.raises(Exception) as e:
        _ = x.div(y)
    assert str(e.value) == "The scale factor is differ between 100 and 10."
