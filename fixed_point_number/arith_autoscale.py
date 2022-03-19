from .fixed_point_number import FixedPointNumber
import logging
import math

logger = logging.getLogger(__name__)


def _check(x, y):
    if not (isinstance(x, FixedPointNumber)):
        raise TypeError("value must be a FixedPointNumber.")
    if not (isinstance(y, FixedPointNumber)):
        raise TypeError("value must be a FixedPointNumber.")


def _calc_scale_factor(x: FixedPointNumber, y: FixedPointNumber):
    lcm = math.lcm(x.scale, y.scale)
    return (lcm, lcm // x.scale, lcm // y.scale)


def add(x: FixedPointNumber, y: FixedPointNumber):
    _check(x, y)
    (scale, x_mul, y_mul) = _calc_scale_factor(x, y)
    logger.debug(f"scale: {scale}, x_mul: {x_mul}, y_mul: {y_mul}")
    internal = x.internal * x_mul + y.internal * y_mul
    return FixedPointNumber(internal, scale)


def sub(x: FixedPointNumber, y: FixedPointNumber):
    _check(x, y)
    (scale, x_mul, y_mul) = _calc_scale_factor(x, y)
    logger.debug(f"scale: {scale}, x_mul: {x_mul}, y_mul: {y_mul}")
    internal = x.internal * x_mul - y.internal * y_mul
    return FixedPointNumber(internal, scale)


def mul(x: FixedPointNumber, y: FixedPointNumber):
    _check(x, y)
    (scale, x_mul, y_mul) = _calc_scale_factor(x, y)
    logger.debug(f"scale: {scale}, x_mul: {x_mul}, y_mul: {y_mul}")
    internal_mul = x.internal * x_mul * y.internal * y_mul
    (internal, surplus) = divmod(internal_mul, scale)
    logger.debug(f"internal: {internal}, surplus: {surplus}")
    if not 0 == surplus:
        logger.warning(f"drop surplus: {surplus / (scale ** 2)}")
    return FixedPointNumber(internal, scale)


def div(x: FixedPointNumber, y: FixedPointNumber):
    _check(x, y)
    (scale, x_mul, y_mul) = _calc_scale_factor(x, y)
    logger.debug(f"scale: {scale}, x_mul: {x_mul}, y_mul: {y_mul}")
    (internal, surplus) = divmod(x.internal * x_mul * scale, y.internal * y_mul)
    logger.debug(f"internal: {internal}, surplus: {surplus}")
    if not 0 == surplus:
        logger.warning(f"drop surplus: {surplus / (scale ** 2)}")
    return FixedPointNumber(internal, scale)
