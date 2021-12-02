from typing import Generator

def pow_twelve(max_pow: int) -> Generator:
    cur_pow: int = 1
    while cur_pow * cur_pow <= max_pow:
        yield cur_pow * cur_pow
        cur_pow += 1

for item in pow_twelve(int(input())):
    print(item)