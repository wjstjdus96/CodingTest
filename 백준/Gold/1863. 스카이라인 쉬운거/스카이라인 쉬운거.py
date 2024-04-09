import sys
input = sys.stdin.readline

n = int(input())
stack = []
cnt = 0
for _ in range(n):
    x,y = map(int,input().split())
    while stack and stack[-1][1] > y:
        stack.pop()
        cnt += 1
    if y == 0:
        stack = []
        continue
    if not stack or stack[-1][1] != y:
        stack.append((x,y))
print(cnt+len(stack))