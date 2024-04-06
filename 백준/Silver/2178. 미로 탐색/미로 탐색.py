from collections import deque
N, M = map(int,input().split())
board = []

for _ in range(N):
    board.append(list(input()))

start = (0,0)
end = (N-1,M-1)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

visited = [[0] * M for _ in range(N)]
queue = deque([start])

while queue:
    x, y = queue.popleft()
    if (x,y) == end:
        print(visited[x][y]+1)
        break
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == "1" and visited[nx][ny] ==0:
            queue.append((nx,ny))
            visited[nx][ny] = visited[x][y] + 1