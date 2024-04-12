from heapq import *
import sys
input = sys.stdin.readline

def dijkstra(start):
    q = []
    distance[start] = 0
    heappush(q,(0,start))
    
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heappush(q,(cost,i))

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [int(1e9)]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

dijkstra(x)

ans = []
for i in range(1, n+1):
    if distance[i] == k:
        ans.append(str(i))

print("\n".join(ans) if len(ans) != 0 else -1)