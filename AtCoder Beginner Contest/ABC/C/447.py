s = input()
t = input()

ss = s.replace("A", "")
tt = t.replace("A", "")
# print(ss)
# print(tt)

if ss != tt:
    print(-1)
else:
    s_list = [0] * (len(ss) + 1)
    t_list = [0] * (len(tt) + 1)
    cnt = 0
    for sss in s:
        if sss != "A":
            cnt += 1
        else:
            s_list.append(sss)
            cnt = 0
    cnt = 0
    for ttt in t:
        if ttt != "A":
            cnt += 1
        else:
            t_list.append(sss)
            cnt = 0
    for i in range(s_list)