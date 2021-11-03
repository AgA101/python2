class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Vector(Point):
    def __init__(self, x, y,quantity):
        super().__init__(x, y)
        self.quantity = quantity

class Vehicle:
    def __init__(self,vectors):
        self.vectors = vectors

    #def distance(self):
    #    return sum(self).x




kol = 2
vectors = []
for i in range(kol):
    x,y,quantity = [int(x) for x in input().split()]
    vectors.append(Vector(x,y,quantity))
way = Vehicle(vectors)
print(way.distance())
for i in range(kol):
    print(way.vectors[i].x,way.vectors[i].y,way.vectors[i].quantity)

class Car:
    #def __init__(self,x,y):
    pass
