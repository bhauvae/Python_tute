class Shape:
    def __init__(self, colour="White"):
        self.__colour = colour

    def get_colour(self):
        return self.__colour

    def set_colour(self, new_colour):
        self.__colour = new_colour


class Circle(Shape):

    def __init__(self, radius=1):
        super().__init__()
        self.radius = radius

    def get_area(self):
        return 3.14 * (self.radius ** 2)


        


class Rectangle(Shape):

    def __init__(self, colour,length=1, breadth=1):
        super().__init__(colour)
        self.length = length
        self.breadth = breadth

    def get_area(self):
        return self.length * self.breadth


r = Rectangle(2, 2)

print(r.get_area())
print(r.get_colour())
