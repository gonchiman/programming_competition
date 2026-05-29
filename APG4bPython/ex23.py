from functools import cache

N = int(input())

@cache
def func(x):
    if x == 0:
        return 1
    else:
        return func(int(x/2)) + func(int(x/3)) + func(int(x/5))
    
print(func(N))