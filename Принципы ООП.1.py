class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def distance(self):
        return ((self.x) ** 2 + (self.y) ** 2) ** 0.5

    def summ(self, other):
        return self.x + other.x, self.y + other.y

    def minus(self, other):
        return self.x - other.x, self.y - other.y

    def miltiplication_on_number(self, number):
        return self.x * number, self.y * number

    def miltiplication_on_vector(self,vector):
        return self.x * vector.x + self.y * vector.y


ver1 = Vector(1,2)
ver2 = Vector(2,3)
print(ver1.miltiplication_on_number(4))
print(ver1.miltiplication_on_vector(ver2))