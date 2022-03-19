from fixed_point_number import __version__, FixedPointNumber


def test_version():
    assert __version__ == "0.1.0"


def test_FixedPointNumber():
    assert FixedPointNumber()
