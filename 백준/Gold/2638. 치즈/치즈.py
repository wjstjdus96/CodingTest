import sys
input = sys.stdin.readline


def find(x,y):
    q = []
    q.append([x,y])
    board[x][y] = 5

    while q:
        cur = q.pop()
        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny] != 5:
                if board[nx][ny] == 1:
                    board[nx][ny] = 2
                elif board[nx][ny] == 2:
                    board[nx][ny] = 3
                elif board[nx][ny] == 0:
                    board[nx][ny] = 5
                    q.append([nx,ny])
def melt():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 5:
                board[i][j] = 0
            if board[i][j] == 2:
                board[i][j] = 1
            if board[i][j] == 3:
                cnt += 1
                board[i][j] = 0
    return cnt

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
time = 0
cnt = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

while True:
    find(0,0)
    cnt = melt()
    if cnt == 0:break
    time += 1

print(time)