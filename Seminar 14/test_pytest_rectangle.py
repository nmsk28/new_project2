# Test class Rectangle option: pytest
import pytest


class Rectangle:
    def __init__(self, length: float, width: float | None = None) -> None:
        self.length = length
        self.width = width
        # if self.width <= 0 or length <= 0:
        #     raise f'You cannot create a rectangle with sides of negative length.'
        if self.width:
            self.width = width
        else:
            self.width = length

    def check_if_valid(self) -> bool:
        return self.width > 0 and self.length > 0

    def get_length(self) -> float:
        return 2 * (self.length + self.width)

    def get_area(self) -> float:
        return self.width * self.length


res1 = Rectangle(4, 5)
res2 = Rectangle(3, 8)
res4 = Rectangle(-1, 8)


def test_check_is_valid():
    assert res1.check_if_valid(), 'Should be True'


def test_check_is_valid_2():
    assert res4.check_if_valid() == False, 'Should be False'


def test_get_length():
    assert res1.get_length() == 18.0, 'Should be 18.0'


def test_get_area():
    assert res2.get_area() == 24.0, 'Should be 24.0'


if __name__ == '__main__':
    pytest.main()
