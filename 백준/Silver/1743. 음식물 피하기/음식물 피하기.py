def dfs(s):
    stack = [s]
    visited[s[0]][s[1]] = 1
    area = 1

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while stack:
        x,y = stack.pop()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<nx<=n and 0<ny<=m and visited[nx][ny] == 0 and food_waste[nx][ny] == 1:
                stack.append((nx,ny))
                visited[nx][ny] = 1
                area += 1
    return area

n,m,k = map(int,input().split())
visited = [[0]*(m+1)for _ in range(n+1)]
food_waste = [[0]*(m+1) for _ in range(n+1)]
result =[]

for i in range(k):
    x,y = map(int, input().split())
    food_waste[x][y] = 1

for i in range(1,n+1):
    for j in range(1,m+1):
        if visited[i][j] == 0 and food_waste[i][j] == 1:
            size = dfs((i,j))
            result.append(size)

print(max(result))