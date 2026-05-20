n = int(input())
inputs = list()

for _ in range(n):
    a, b = map(int, input().split())
    inputs.append([a, b])

for input in inputs:
    print(sum(input))