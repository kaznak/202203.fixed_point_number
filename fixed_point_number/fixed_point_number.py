import logging

logger = logging.getLogger(__name__)


class FixedPointNumber:
    def __init__(self, internal_value: int, scaling_factor: int):
        if scaling_factor < 1:
            raise ValueError("scaling factor must be a positive integer.")
        self.internal = internal_value
        self.scale = scaling_factor

    def _check(self, x):
        if not (isinstance(x, FixedPointNumber)):
            raise TypeError("value must be a FixedPointNumber.")
        if not (x.scale == self.scale):
            raise ValueError(
                f"The scale factor is differ between {self.scale} and {x.scale}."
            )

    def add(self, x):
        self._check(x)
        self.internal += x.internal
        return self

    def sub(self, x):
        self._check(x)
        self.internal -= x.internal
        return self

    def mul(self, x):
        self._check(x)
        internal_mul = self.internal * x.internal
        (internal, surplus) = divmod(internal_mul, self.scale)
        if not 0 == surplus:
            logger.warning(f"drop surplus: {surplus / (self.scale ** 2)}")
        self.internal = internal
        return self
