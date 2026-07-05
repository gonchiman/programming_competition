n = int(input())
s = input()
a, b = [], []
rev = False
for i in range(n):
    print(f"i: {i}")
    print(f"rev: {rev}")
    print(f"s[i]: {s[i]}")
    if rev:
        a.append(i + 1)
    else:
        b.append(i + 1)
    if s[i] == "o":
        rev ^= True
    print(f"a: {a}")
    print(f"b: {b}")
    print()
ans = a[::-1] + b
print(f"ans: {ans}")
print(f"rev: {rev}")
if rev:
    ans = ans[::-1]
print(f"ans: {ans}")
print("\n[answer]")
print(*ans)
