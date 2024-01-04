#!/usr/bin/python3

"""This is my class."""


class Rectangle:
    """Rectangle class.

    Methods:
    __init__: To initialize new instances.
    width: To get or set width.
    Height: To get or set height.
    """

    @classmethod
    def square(cls, size=0):
        """Make square instance out of rectangle class."""
        new_square = Rectangle(size, size)
        return new_square

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Determine which rectangle is bigger."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        rect1_area = rect_1.area()
        rect2_area = rect_2.area()
        if rect1_area == rect2_area:
            return rect_1
        elif rect1_area > rect2_area:
            return rect_1
        else:
            return rect_2

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize new instances.

        Parameters:
        - width (int): Width of the rectangle.
        - height (int): Height of the rectangle.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """To get width."""
        return self.__width

    @width.setter
    def width(self, value):
        """To set Width.

        Parameters:
        - value (int): New value of width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """To get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """To set the height.

        Parameters:
        - value (int): The new value of height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Area of the rectangle."""
        return int(int(self.__width) * int(self.__height))

    def perimeter(self):
        """Perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return int(2 * (int(self.__width) + int(self.__height)))

    def __str__(self):
        """Str function."""
        result = ""
        for _ in range(self.__height):
            for _ in range(self.__width):
                result += str(self.print_symbol)
            result += "\n"
        return result.strip()

    def __repr__(self):
        """Repr function."""
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        """Del function."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
