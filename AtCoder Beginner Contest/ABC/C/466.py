n = int(input())

def ask(i, j):
    print(f"? {i} {j}")
    print()

def kaijou(x):
    kaijou = 1
    for i in range(x):
        i = i + 1
        kaijou *= i
    return kaijou

x = 0
res = 0
for i in range(n):
    if x == 0:
        break
    i = i + 1
    for j in range(n, x, -1):
        j = j + 1
        ask(i, j)
        judge = input()
        if judge == "Yes":
            x = n - j
            if j - i == 1:
                res += 1
            else:
                res += kaijou(j-i) / 2
            break
        if judge == "No":
            