class Shape:
    def set_importance(self, string):
        pass


class Rectangle(Shape):

    def set_importance(self, string):
        print(string)


class Square(Shape):
    def set_importance(self, string):
        print(string)


class Triangle(Shape):
    def set_importance(self, string):
        print(string)
        pass

    pass


class Abstraction:
    rectangle = Rectangle()
    rectangle.set_importance('important')

    square = Square()
    square.set_importance('not important')

    triangle = Triangle()
    triangle.set_importance('this will print')
