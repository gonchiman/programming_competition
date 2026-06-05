S = input()
N = int(input())


result = str()

for i, s in enumerate(S):
    if i < N:
        continue
    elif i > len(S) - (N + 1):
        continue
    else:
        result += s

print(result)