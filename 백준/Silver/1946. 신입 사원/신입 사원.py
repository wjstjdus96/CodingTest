import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    score = []

    for _ in range(n):
        score.append((list(map(int,input().split()))))
    score.sort()

    cnt = 0
    min = float('inf')
    for i in range(0,n):
        if score[i][1] < min:
            min = score[i][1]
            cnt += 1

    print(cnt)