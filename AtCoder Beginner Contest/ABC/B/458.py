H, W = map(int, input().split())


for i in range(H):
    row = list()
    for j in range(W):
        if H == 1:
            if W == 1:
                row.append("0")
            elif j == 0 or j == W-1:
                row.append("1")
            else:
                row.append("2")
        elif W == 1:
            if i == 0 or i == H-1:
                row.append("1")
            else:
                row.append("2")
        else:
            if i == 0:
                if j == 0 or j == W-1:
                    row.append("2")
                else:
                    row.append("3")
            elif i == H-1:
                if j == 0 or j == W-1:
                    row.append("2")
                else:
                    row.append("3")
            elif j == 0 or j == W-1:
                row.append("3")
            else:
                row.append("4")

    print(" ".join(row))