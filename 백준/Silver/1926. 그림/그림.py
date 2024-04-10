import sys
input = sys.stdin.readline

def dfs(drawing, start):
    global visited
    visited[start[0]][start[1]] = 1
    stack = [start]
    area = 1

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0 and drawing[nx][ny] == "1":
                stack.append((nx,ny))
                visited[nx][ny] = 1
                area += 1
    return area


n,m = map(int,input().split())
drawing = []
visited = [[0]*m for _ in range(n)]
tot_cnt = 0
max_area = 0

for _ in range(n):
    drawing.append(list(input().split()))

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and drawing[i][j] == "1":
            area = dfs(drawing,(i,j))
            tot_cnt += 1
            max_area = max(max_area, area)

print(tot_cnt)
print(max_area)