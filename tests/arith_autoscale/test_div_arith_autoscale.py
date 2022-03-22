import pytest

from fixed_point_number import FixedPointNumber
from fixed_point_number.arith_autoscale import div

from logging import WARNING, getLogger

logger = getLogger(__name__)


def test_FixedPointNumber_div_000():
    x = FixedPointNumber(100, 100)
    y = FixedPointNumber(100, 100)
    z = div(x, y)
    assert z.internal == 100
    assert z.scale == 100


def test_FixedPointNumber_div_001(caplog):
    caplog.set_level(WARNING)
    x = FixedPointNumber(10000, 100)
    y = FixedPointNumber(300, 100)
    z = div(x, y)
    assert z.internal == 3333
    assert z.scale == 100
    assert caplog.record_tuples == [
        ("fixed_point_number.arith_autoscale", WARNING, "drop surplus: 0.01")
    ]


def test_FixedPointNumber_div_002(caplog):
    caplog.set_level(WARNING)
    x = FixedPointNumber(10000, 100)
    y = FixedPointNumber(-300, 100)
    z = div(x, y)
    assert z.internal == -3334
    assert z.scale == 100
    assert caplog.record_tuples == [
        ("fixed_point_number.arith_autoscale", WARNING, "drop surplus: -0.02")
    ]


def test_FixedPointNumber_div_003():
    x = FixedPointNumber(100, 100)
    y = FixedPointNumber(100, 10)
    z = div(x, y)
    assert z.internal == 10
    assert z.scale == 100


def test_FixedPointNumber_div_100():
    x = FixedPointNumber(100, 100)
    y = 1
    with pytest.raises(Exception) as e:
        _ = div(x, y)
    assert str(e.value) == "value must be a FixedPointNumber."
