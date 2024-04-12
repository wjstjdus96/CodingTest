import sys
input = sys.stdin.readline

n, m = map(int,input().split())
table = []
for _ in range(n):
    table.append(list(map(int,input().split())))

for j in range(n):
    for i in range(1, n):
        table[i][j] += table[i-1][j]

for i in range(n):
    for j in range(1, n):
        table[i][j] += table[i][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1

    if x1 == 0 and y1 == 0:
        result = table[x2][y2]
    elif x1 == 0:
        result = table[x2][y2] - table[x2][y1-1]
    elif y1 == 0:
        result = table[x2][y2] - table[x1-1][y2]
    else:
        result = table[x2][y2] - table[x2][y1-1] - table[x1-1][y2] + table[x1-1][y1-1]

    print(result)