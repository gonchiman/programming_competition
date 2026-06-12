H, W = map(int, input().split())


for i in range(H):
    row = str()
    for j in range(W):
        if i == 0 or i == H-1:
            row += "#"
        elif j == 0 or j == W-1:
            row += "#"
        else:
            row += "."
    
    print(row)