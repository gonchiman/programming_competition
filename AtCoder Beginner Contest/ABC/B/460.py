import math
from decimal import Decimal, getcontext

getcontext().prec = 50

T = int(input())
CASES = list()
for _ in range(T):
    CASES.append([int(x) for x in input().split()])


def is_intersection(case: list) -> bool:
    rs = float(case[2] + case[5])
    d = (Decimal(abs(case[3] - case[0]) ** 2 + abs(case[4] - case[1]) ** 2)).sqrt()

    if d < case[2] and (d + case[5]) < case[2]:
        return False
    elif d < case[5] and (d + case[2]) < case[5]:
        return False

    if rs >= d:
        return True
    else:
        return False
    
    

for i in range(T):
    if is_intersection(CASES[i]):
        print("Yes")
    else:
        print("No")