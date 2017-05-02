class Point:
    # Represents a point in two-dimensional geometric coordinates

    def __init__(self, x=0, y=0):
        # Initialize the position of a new point. The x and y coordinates could
        # be specified. If they are not, the point defaults to the origin.
        self.move(x, y)

    def move(self, x, y):
        # Move the point to a new location in 2D space.
        self.x = x
        self.y = y


class Triangle:
    # Class for triangles

    def __init__(self, a, b, c):
        # Initialises triangle by three variables of class Point
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def sidelen(a, b):
        # Finds distance between two variables of class Point
        return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5

    def perimeter(self):
        # Finds perimeter of a triangle using function sidelen
        return self.sidelen(self.a, self.b) + self.sidelen(self.c, self.b) \
               + self.sidelen(self.a, self.c)

    def area(self):
        # Finds area of a triangle using Heron`s formula
        # Return False if area equals 0, True otherwise
        p = self.perimeter() / 2
        try:
            # If two points are the same area could turn out to be sqrt(-...)
            # and an error will occur
            ar = round((p * (p - self.sidelen(self.a, self.b)) *
                        (p - self.sidelen(self.a, self.c)) *
                        (p - self.sidelen(self.c, self.b))) ** 0.5, 3)
            return True if ar != 0 else False
        except TypeError:
            return False


def mult_diff(a, b):
    # Function to avoid copy/paste
    # Counts (x1-x2)*(y3-y4)-(x3-x4)*(y1-y2)
    return a[0] * b[1] - a[1] * b[0]


def line_intersect(coords1, coords2):
    # Checks if two lines defined by 2 points intersect or are parallel or collinear
    triangle1 = Triangle(Point(coords1[0][0], coords1[0][1]),
                         Point(coords1[1][0], coords1[1][1]),
                         Point(coords2[1][0], coords1[1][1]))
    triangle2 = Triangle(Point(coords1[0][0], coords1[0][1]),
                         Point(coords1[1][0], coords1[1][1]),
                         Point(coords2[0][0], coords1[0][1]))

    if triangle1.area() is False and triangle2.area() is False:
        return coords1
    len_x = (coords1[0][0] - coords1[1][0], coords2[0][0] - coords2[1][0])
    len_y = (coords1[0][1] - coords1[1][1], coords2[0][1] - coords2[1][1])

    relation = mult_diff(len_x, len_y)
    if relation == 0:
        return None
    else:
        d = (mult_diff(*coords1), mult_diff(*coords2))
        x = mult_diff(d, len_x) / relation
        y = mult_diff(d, len_y) / relation
        return round(x, 3), round(y, 3)

print(line_intersect(((0, 0), (0, 1)), ((1, 1), (1, 0))))
