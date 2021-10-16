class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

row = list(map(int, input().split()))
row2 = list(map(int, input().split()))
c1 = Circle(row[0],row[1],row[2])
c2 = Circle(row2[0],row2[1],row2[2])
r = ((c1.x - c2.x) ** 2 + (c1.y - c2.y) ** 2) ** 0.5
if (c1.r + c2.r >= r and r + c2.r >= c1.r and r + c1.r >= c2.r):
    print('YES')
else:
    print('NO')