N, X = input().split()
S = [input() for _ in range(int(N))]


match X:
    case "A":
        X = 1
    case "B":
        X = 2
    case "C":
        X = 3
    case "D":
        X = 4
    case "E":
        X = 5


is_empty = False
for s in S:
    if s[X - 1] == "o":
        print("Yes")
        is_empty = True
        break

if not is_empty:
    print("No")