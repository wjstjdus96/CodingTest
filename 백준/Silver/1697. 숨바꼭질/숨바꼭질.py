from collections import deque
import sys
input=sys.stdin.readline

n,k=map(int,input().split())

def bfs(n,k):
    queue = deque([(n,0)])
    visited = [False]*(100000+1)
    visited[n] = True

    while queue:
        node,time = queue.popleft()
        possible_routes = [node-1, node+1, node*2]
        if node == k:
            return time
        for new in possible_routes:
            if 0<=new<=100000 and not visited[new] :
                queue.append((new,time+1))
                visited[new] = True

print(bfs(n,k))