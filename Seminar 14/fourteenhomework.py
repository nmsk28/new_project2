'''
'''
'''
Урок 14. Основы тестирования
Возьмите class Rectangle. Напишите к нему тесты. 2-5 тестов на задачу 
в трёх вариантах: doctest, unittest, pytest.
'''

# Test class Rectangle option: doctest
class NegativeRangeSide(Exception):
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def __str__(self):
        return f'You cannot create a rectangle with sides of negative length.'


class Rectangle:
    ''' Compute and return the perimeter and area of a rectangle'''

    def __init__(self, length: float, width: float | None = None) -> None:
        self.length = length
        self.width = width
        if self.width <= 0 or self.length <= 0:
            raise NegativeRangeSide(width, length)
        if self.width:
            self.width = width
        else:
            self.width = length

    def get_length(width, length) -> float:
        '''Compute and return the perimeter of a rectangle

        Usage examples:
        >>> Rectangle.get_length(4.0,5.0)
        18.0

        The output must be an float:
        >>> Rectangle.get_length(7.0,5.0)
        24.0
        '''
        return 2 * (length + width)

    def get_area(width, length) -> float:
        '''Compute and return the area of a rectangle

        Usage examples:
        >>> Rectangle.get_area(4.0,5.0)
        20.0

        The output must be an float:
        >>> Rectangle.get_area(7.0,5.0)
        35.0
        '''
        return width * length


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


# Test class Rectangle option: unittest


import unittest


class NegativeRangeSide(Exception):
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def __str__(self):
        return f'You cannot create a rectangle with sides of negative length.'


class Rectangle:
    ''' Compute and return the perimeter and area of a rectangle'''

    def __init__(self, length: float, width: float | None = None) -> None:
        self.length = length
        self.width = width
        # if self.width <= 0 or self.length <= 0:
        #     raise NegativeRangeSide(length, width)
        if self.width:
            self.width = width
        else:
            self.width = length

    def __str__(self):
        return f'{self.length} {self.width}'

    def get_length(self) -> float:
        return 2 * (self.length + self.width)

    def get_area(self) -> float:
        return self.width * self.length

    def check_if_valid(self) -> bool:
        return self.width > 0 and self.length > 0


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect1 = Rectangle(-2, 3)
        self.rect2 = Rectangle(3, 3)
        self.rect3 = Rectangle(7, 5)

    def test_get_length(self):
        self.assertEqual(24.0, self.rect3.get_length(), "Should be 24.0")

    def test_get_area(self):
        self.assertEqual(35.0, self.rect3.get_area(), "Should be 35.0")

    def test_check_is_valid(self):
        self.assertFalse(self.rect1.check_if_valid(), "Both width and length must be positive")

    def test_check_is_valid(self):
        self.assertTrue(self.rect3.check_if_valid(), "Both width and length must be positive")


if __name__ == '__main__':
    unittest.main()
