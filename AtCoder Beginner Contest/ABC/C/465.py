n = int(input())
s = input()

res = [str(i + 1) for i in range(n)]
for k in range(n):
    if s[k] == "o" and k != 0:
        temp = res[0:k+1]
        for i in range(int((k+1)/2)):
            left = temp[i]
            right = temp[-i-1]
            temp[i] = right
            temp[-i-1] = left
        res[0:k+1] = temp
    # print(k)
    # print(res)
    # print()

res = " ".join(res)
print(res)