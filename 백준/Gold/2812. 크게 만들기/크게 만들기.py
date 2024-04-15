import sys
input = sys.stdin.readline

n,k = map(int,input().split())
number = list(input().strip())
cnt = k
stack = []

for i in number:
    i = int(i)
    while stack and i > stack[-1] and cnt > 0:
        stack.pop()
        cnt -= 1
    stack.append(i)


if cnt != 0:
    for i in range(cnt):
        stack.pop()

print("".join(map(str,stack)))