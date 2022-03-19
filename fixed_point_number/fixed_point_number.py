import logging

logger = logging.getLogger(__name__)


class FixedPointNumber:
    def __init__(self, internal_value: int, scaling_factor: int):
        if scaling_factor < 1:
            raise ValueError("scaling factor must be a positive integer.")
        self.internal = internal_value
        self.scale = scaling_factor
