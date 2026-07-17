n = int(input())

l = 1
r = 2
ans = 0

while r <= n:
    print(f"? {l} {r}")
    s = input()
    if s == "Yes":
        r += 1
    else:
        ans += r - l -1
        l += 1
        if l == r:
            r += 1

while l < n:
    ans += r - l - 1
    l += 1

print(f"! {ans}")