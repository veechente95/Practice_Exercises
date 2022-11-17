from prettytable import PrettyTable

# TODO: Design a few classes that represent the following geometric figures (circle, square).
#  They should do the following member functions --> get_area and get_volume.
#  Each class should have constructor (eg __init__) method that instantiate data the class should keep track of.

# circle area = πr^2
# circle volume (cylinder) = πr2h
# square area = side^2
# square volume = side^3


class Circle:
    def __init__(self):
        self.area = circle_get_area
        self.volume = circle_get_volume


class Square:
    def __init__(self):
        self.area = square_get_area
        self.volume = square_get_volume


pi = 3.14
radius = float(input("What is the radius of circle: "))
height = float(input("What is the height of your circle: "))
circle_get_area = pi * radius ** 2
circle_get_volume = pi * radius * 2 * height

side = int(input("How many sides does your square have?: "))
square_get_area = side ** 2
square_get_volume = side ** 3

# Creates a cleaner print layout 
table = PrettyTable()
table.align = "l"
table.add_column("Circle Area & Volume", [f"Your circle area is {circle_get_area}", f"Your circle volume is {circle_get_volume}"])
table.add_column("Square Area & Volume", [f"Your square area is {square_get_area}", f"Your square volume is {square_get_volume}"])
print(table)
