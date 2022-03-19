from .fixed_point_number import FixedPointNumber
import logging
import math

logger = logging.getLogger(__name__)


def _check(x, y):
    if not (isinstance(x, FixedPointNumber)):
        raise TypeError("value must be a FixedPointNumber.")
    if not (isinstance(y, FixedPointNumber)):
        raise TypeError("value must be a FixedPointNumber.")
    if not (x.scale == y.scale):
        raise ValueError(f"The scale factor is differ: {x.scale} and {y.scale}.")


def add(x: FixedPointNumber, y: FixedPointNumber):
    _check(x, y)
    scale = x.scale
    internal = x.internal + y.internal
    return FixedPointNumber(internal, scale)


def sub(x: FixedPointNumber, y: FixedPointNumber):
    _check(x, y)
    scale = x.scale
    internal = x.internal - y.internal
    return FixedPointNumber(internal, scale)


def mul(x: FixedPointNumber, y: FixedPointNumber):
    _check(x, y)
    scale = x.scale
    (internal, surplus) = divmod(x.internal * y.internal, scale)
    logger.debug(f"internal: {internal}, surplus: {surplus}")
    if not 0 == surplus:
        logger.warning(f"drop surplus: {surplus / (scale ** 2)}")
    return FixedPointNumber(internal, scale)


def div(x: FixedPointNumber, y: FixedPointNumber):
    _check(x, y)
    scale = x.scale
    (internal, surplus) = divmod(x.internal * scale, y.internal)
    logger.debug(f"internal: {internal}, surplus: {surplus}")
    if not 0 == surplus:
        logger.warning(f"drop surplus: {surplus / (scale ** 2)}")
    return FixedPointNumber(internal, scale)
