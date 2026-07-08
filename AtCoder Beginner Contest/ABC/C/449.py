n, l, r = map(int, input().split())
s = input()

d = {}
for c in s:
    d[c] = 0
# print(d)

ans = 0
for i, c in enumerate(s):
    # print(f"i: {i}") ##
    # print(f"s[i]: {s[i]}") ##
    if i >= l:
        d[s[i-l]] += 1
    if i > r:
        d[s[i-(r+1)]] -= 1
    # print(f"d: {d}") ##
    # print() ##
    ans += d[s[i]]
print(ans)