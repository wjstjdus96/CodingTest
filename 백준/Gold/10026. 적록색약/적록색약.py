import sys
input = sys.stdin.readline

def dfs(g,v,n):
    global visited
    stack = [v]
    visited[v[0]][v[1]] = True

    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    while stack:
        x,y = stack.pop()
        now_color = g[x][y]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0 <=ny<n and not visited[nx][ny] and g[nx][ny] == now_color:
                stack.append((nx,ny))
                visited[nx][ny] = True

def count_color(graph,cnt):
    global visited,n
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                dfs(graph,(i,j),n)
                cnt+=1
    return cnt


n = int(input())
colors = [list(input()) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
cnt = count_color(colors, 0)

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if colors[i][j]=='R':
            colors[i][j]='G'
cnt_rg = count_color(colors, 0)

print(cnt, cnt_rg)