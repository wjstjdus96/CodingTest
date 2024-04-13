from collections import defaultdict
import sys
input = sys.stdin.readline

n, m, r = map(int,input().split())
graph = [[] for _ in range(n+1)]
order = {key:0 for key in range(1,n+1)}

for _ in range(m):
    n1,n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(1, n+1):
    graph[i].sort(reverse=False)

def dfs(g, v):
    visited = [False]*(n+1)
    stack = [v]
    cnt = 0

    while stack:
        now = stack.pop()
        if not visited[now]:
            visited[now] = True
            cnt += 1
            order[now] = cnt
        for i in g[now]:
            if not visited[i]:
                stack.append(i)
    return order

answer = dfs(graph,r)
print("\n".join(map(str,answer.values())))