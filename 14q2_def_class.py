class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def ex_width(self):
        self.width *= 2

    def ex_height(self):
        self.height *= 2


rectangle = Rectangle(3, 4)
print(rectangle.get_area())
rectangle.ex_height()
rectangle.ex_width()
print(rectangle.width, rectangle.height)
