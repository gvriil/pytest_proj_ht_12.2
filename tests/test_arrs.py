from utils import arrs


def test_get(create_set):
    assert arrs.get(create_set, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(create_set):
    assert arrs.my_slice(create_set, 1, 3) == [2, 3]
    assert arrs.my_slice(create_set, 1) == [2, 3, 4]
    assert arrs.my_slice(create_set, 3, 1) == []
    assert arrs.my_slice(create_set, 1, -1) == [2, 3]
    assert arrs.my_slice(create_set, 1, 5) == [2, 3, 4]
    assert arrs.my_slice([], 0, 0) == []
    assert arrs.my_slice(create_set) == [1, 2, 3, 4]
