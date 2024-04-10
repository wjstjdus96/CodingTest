import sys
input = sys.stdin.readline
from collections import deque

def bfs(v):
    queue = deque([v])
    cnt = 1
    visited = [False] * (n+1)
    visited[v] = True
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                cnt += 1
    return cnt

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
result = []

for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

for i in range(1,n+1):
    result.append(bfs(i))

max_result = max(result)
for i, r in enumerate(result):
    if r == max_result:
        print(i+1, end=" ")