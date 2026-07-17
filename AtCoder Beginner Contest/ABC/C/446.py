from collections import deque

t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = deque()

    for i in range(n):
        aa = a[i]
        bb = b[i]
        today = i + 1

        q.extend([today] * aa)
        for j in range(bb):
            q.popleft()

        if today >= d:
            count = 0
            for qq in q:
                if qq == today - d:
                    count += 1
                else:
                    break
            for _ in range(count):
                q.popleft()
    
    res = len(q)
    print(res)