import sys
input = sys.stdin.readline

def dfs(s):
    stack = [s]
    
    while stack:
        cur = stack.pop()
        if visited[cur] == 0:
            visited[cur] = 1
            for node in graph[cur]:
                if visited[node] == 0:
                    stack.append(node)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
cnt = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    if visited[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)
