N = int(input())
map_list = [list(input()) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = []

visited = []
for i in range(N):
    for j in range(N):
        if (i,j) not in visited and map_list[i][j] == "1":
            stack = [(i,j)]
            visited.append((i,j))
            cnt = 1
            while stack:
                x, y = stack.pop()
                for idx in range(4):
                    nx, ny = x+dx[idx], y+dy[idx]
                    if 0 <= nx < N and 0<= ny < N and map_list[nx][ny] == "1" and (nx,ny) not in visited:
                        stack.append((nx,ny))
                        visited.append((nx,ny))
                        cnt += 1
            answer.append(cnt)
    

print(len(answer))
print("\n".join(list(map(str,sorted(answer)))))