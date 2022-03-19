class FixedPointNumber:
    def __init__(self, num: int, q: int):
        assert q >= 0
        self.num = num
        self.q = q
