from heapq import heappop, heappush

que = []
q = int(input())
for i in range(q):
    t, h = map(int, input().split())
    if t == 1:
        heappush(que, h)
    else:
        while que and que[0] <= h:
            heappop(que)
    print(len(que))
