from prettytable import PrettyTable

# TODO: Design a few classes that represent the following geometric figures (circle, square).
#  They should do the following member functions --> get_area and get_volume.
#  Each class should have constructor (eg __init__) method that instantiate data the class should keep track of.

# circle area = πr^2
# circle volume (cylinder) = πr2h
# square area = side^2
# square volume = side^3


class Circle:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    # define get_area and get_volume functions
    def get_area(self):
        return PI * self.radius ** 2

    def get_volume(self):
        return PI * self.radius * 2 * self.height


class Square:
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

    def get_volume(self):
        return self.side ** 3


print("Let's find the area and volume of your circle and square.")
PI = 3.14
RADIUS = float(input("What is the radius of your circle: "))
HEIGHT = float(input("What is the height of your circle: "))
SIDE = int(input("What is the length of your square's sides?: "))

circle_instance = Circle(RADIUS, HEIGHT)
square_instance = Square(SIDE)

table = PrettyTable()
table.align = "l"
table.add_column(
    "Circle Area & Volume",
    [
        f"Your circle area is {circle_instance.get_area()}",
        f"Your circle volume is {circle_instance.get_volume()}",
    ],
)
table.add_column(
    "Square Area & Volume",
    [
        f"Your square area is {square_instance.get_area()}",
        f"Your square volume is {square_instance.get_volume()}",
    ],
)
print(table)
