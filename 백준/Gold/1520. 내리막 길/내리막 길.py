import sys
import heapq
input = sys.stdin.readline

def bfs(s_x,s_y):
    heap = [(-table[s_x][s_y],s_x,s_y)]  
    visited[s_x][s_y] = 1

    while heap:
        _,x,y = heapq.heappop(heap)
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if 0<=nx<n and 0<=ny<m and table[nx][ny]<table[x][y]:
                if visited[nx][ny] ==0: 
                    heapq.heappush(heap,(-table[nx][ny],nx,ny))
                visited[nx][ny] += visited[x][y] 

    return visited[n-1][m-1]

n,m = map(int,input().split())
table = [list(map(int,input().split()))for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

print(bfs(0,0))