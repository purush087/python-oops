class Shape:
    def draw_shape(self, color):
        print("shape is in {}".format(color))


class Rectangle(Shape):
    def draw_shape(self, color):
        print('Drawing rectangle of {}'.format(color))


class Square(Shape):
    def draw_shape(self, color):
        print('Drawing Square of {}'.format(color))


class Triangle(Shape):
    pass


class Polymorphism:
    rectangle = Rectangle()
    rectangle.draw_shape('yellow')

    square = Square()
    square.draw_shape('red')

    triangle = Triangle()
    triangle.draw_shape('blue')
