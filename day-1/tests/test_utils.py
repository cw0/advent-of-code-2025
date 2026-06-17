from day_1.utils import right, left

def test_example_behavior():
    assert left(50, 68) == (82, 1)
    assert left(82, 30) == (52, 0)
    assert right(52, 48) == (0, 1)
    assert left(0, 5) == (95, 0)
    assert right(95, 60) == (55, 1)
    assert left(55, 55) == (0, 1)
    assert left(0, 1) == (99, 0)
    assert left(99, 99) == (0, 1)
    assert right(0, 14) == (14, 0)
    assert left(14, 82) == (32, 1)
    assert right(50, 1000) == (50, 10)