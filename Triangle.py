class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        b = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
        c = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
        p = (a + b + c) / 2

        print((p * (p - a) * (p - b) * (p - c)) ** 0.5)

row = list(map(int, input().split()))
tri = Triangle(row[0],row[1],row[2],row[3],row[4],row[5])