N, M = map(int, input().split())
F = list(map(int, input().split()))


set_f = set(F)
print("Yes") if len(set_f) == len(F) else print("No")

is_all_clothes_are_exist = True
for m in range(M):
    m = m + 1
    if m in F:
        continue
    else:
        is_all_clothes_are_exist = False
        break

print("Yes") if is_all_clothes_are_exist else print("No")


# print(f"N, M: {N}, {M}")
# print(f"F: {F}")