import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coin = [int(input()) for _ in range(n)]
cnt = 0

while coin:
    c = coin.pop()
    cnt += k//c
    k = k % c
    
    
print(cnt)