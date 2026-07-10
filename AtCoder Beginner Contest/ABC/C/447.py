s = input()
t = input()

ss = s.replace("A", "")
tt = t.replace("A", "")
# print(f"ss: {ss}")
# print(f"tt: {tt}")

if ss != tt:
    print(-1)
else:
    s_list = []
    t_list = []
    cnt = 0
    for sss in s:
        if sss == "A":
            cnt += 1
        else:
            s_list.append(cnt)
            cnt = 0
    s_list.append(cnt)
    cnt = 0
    for ttt in t:
        if ttt == "A":
            cnt += 1
        else:
            t_list.append(cnt)
            cnt = 0
    t_list.append(cnt)
    # print(f"s_list: {s_list}")
    # print(f"t_list: {t_list}")
    res = 0
    for i in range(len(s_list)):
        res += abs(s_list[i] - t_list[i])
    print(res)