import sys
from heapq import *
input = sys.stdin.readline

def find(s):
    time = 0
    queue = [(0,s)]
    visited = [0]*(n+1)

    while queue:
        cur_time,cur = heappop(queue)
        if visited[cur] == 0:
            time = cur_time
            visited[cur] = 1
            for new_time, new in dep[cur]:
                heappush(queue, (new_time+cur_time, new))

    return sum(visited), time

t = int(input())

for _ in range(t):
    n,d,c = map(int,input().split())
    dep = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    cnt = 1
    time = 0

    for _ in range(d):
        a,b,s = map(int,input().split())
        dep[b].append((s,a))

    res = find(c)
    
    print(res[0],res[1])

    