import pytest

from fixed_point_number import FixedPointNumber
from fixed_point_number.arith_autoscale import mul

from logging import WARNING, getLogger

logger = getLogger(__name__)


def test_FixedPointNumber_mul_000():
    x = FixedPointNumber(100, 100)
    y = FixedPointNumber(100, 100)
    z = mul(x, y)
    assert z.internal == 100
    assert z.scale == 100


def test_FixedPointNumber_mul_001(caplog):
    caplog.set_level(WARNING)
    x = FixedPointNumber(101, 100)
    y = FixedPointNumber(101, 100)
    z = mul(x, y)
    assert z.internal == 102
    assert z.scale == 100
    assert caplog.record_tuples == [
        ("fixed_point_number.arith_autoscale", WARNING, "drop surplus: 0.0001")
    ]


def test_FixedPointNumber_mul_002():
    x = FixedPointNumber(100, 100)
    y = FixedPointNumber(100, 10)
    z = mul(x, y)
    assert z.internal == 1000
    assert z.scale == 100


def test_FixedPointNumber_mul_100():
    x = FixedPointNumber(100, 100)
    y = 1
    with pytest.raises(Exception) as e:
        _ = mul(x, y)
    assert str(e.value) == "value must be a FixedPointNumber."
