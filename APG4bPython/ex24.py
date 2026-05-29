from functools import cache
import sys
sys.setrecursionlimit(10**5)

N = int(input())

def is_odd_popcount(x: int) -> bool:
    return x.bit_count() % 2 == 1

@cache
def func(x: int) -> int:
    if x <= 0:
        return 0
    elif is_odd_popcount(x):
        return func(x - 1) + 1
    else:
        return func(x - 2) + 1

print(func(N))