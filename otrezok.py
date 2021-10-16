class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
row = list(map(int, input().split()))
p1 = Point(row[0],row[1])
p2 = Point(row[2],row[3])
print(((p2.y - p1.y) ** 2 + (p2.x - p1.x) ** 2)  ** 0.5)