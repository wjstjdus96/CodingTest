from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    n1,n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
for i in range(1, n+1):
    graph[i].sort()

def bfs(g, v):
    visited = [False]*(n+1)
    visited[v] = True
    queue = deque([v])
    order = {key:0 for key in range(1,n+1)}
    cnt = 1
    order[v] = cnt

    while queue:
        now = queue.popleft()
        for i in g[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
                order[i] = cnt
    return order

answer = bfs(graph,r)
print("\n".join(map(str,answer.values())))