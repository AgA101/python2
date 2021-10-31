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

    def distance(self):


        #for i in range(len(vectors)):
        #    summ += vectors[i].x
        return min(vectors).x
kol = 2
vectors = [Vector(int(input()),int(input()),int(input())) for i in range(kol)]
way = Vehicle(vectors)
print(way.distance())
#print(vectors[0].x)
class Car:
    #def __init__(self,x,y):
    pass
