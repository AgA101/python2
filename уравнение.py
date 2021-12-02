from typing import Generator

def pow_twelve(a,b,c,d: int) -> Generator:
    x: int = -100
    while x <= 100:
        if a * x ** 3 + b * x ** 2 + c * x + d == 0:
            yield x
        x += 1
a,b,c,d = [int(x) for x in input().split()]
for item in pow_twelve(a,b,c,d):
    print(item,end=' ')