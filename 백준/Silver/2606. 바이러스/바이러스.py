from collections import deque

n = int(input())
net = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(net):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

def bfs(graph,v):
    cnt = 0
    queue = deque([v])
    visited = []
    visited.append(v)

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
                cnt += 1
    return cnt

print(bfs(graph, 1))