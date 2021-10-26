class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #def __copy__(self):

    def distance(self,other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return a.distance(b) + a.distance(c) + b.distance(c)
    def area(self):
        p = (a.distance(b) + a.distance(c) + b.distance(c)) / 2
        return (p * (p - a.distance(b)) * (p - a.distance(c)) * (p - b.distance(c))) ** 0.5
    def contains(self):
        p = (a.distance(b) + a.distance(c) + b.distance(c)) / 2
        p1 = (z.distance(a) + z.distance(b) + a.distance(b)) / 2
        p2 = (z.distance(a) + z.distance(c) + a.distance(c)) / 2
        p3 = (z.distance(b) + z.distance(c) + b.distance(c)) / 2
        if (p * (p - a.distance(b)) * (p - a.distance(c)) * (p - b.distance(c))) ** 0.5 <= \
                ((p1 * (p1 - z.distance(a)) * (p1 - z.distance(b)) * (p1 - a.distance(b))) ** 0.5 + \
                (p2 * (p2 - z.distance(a)) * (p2 - z.distance(c)) * (p2 - a.distance(c))) ** 0.5 + \
                (p3 * (p3 - z.distance(b)) * (p3 - z.distance(c)) * (p3 - b.distance(c))) ** 0.5):
            return "In"
        else:
            return "Out"


a = Point(0,0)
b = Point(3,0)
c = Point(0,4)
z = Point(1,1)
tri = Triangle(a,b,c)
print(tri.contains())
