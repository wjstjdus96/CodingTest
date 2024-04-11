import sys
input = sys.stdin.readline

def bfs(graph,x,y):
    max_distance = 1
    queue = set([(x,y,graph[0][0])])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y, visited = queue.pop()
        if len(visited) > max_distance:
            max_distance = len(visited)		
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c and not graph[nx][ny] in visited: 
                queue.add((nx, ny, visited + graph[nx][ny]))
    return max_distance

r, c = map(int, input().split())
board = [input().rstrip() for _ in range(r)]

answer = bfs(board,0,0)
print(answer)