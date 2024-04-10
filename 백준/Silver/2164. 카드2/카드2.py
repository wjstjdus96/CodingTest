from collections import deque
n = int(input())
queue = deque([i for i in range(1,n+1)])
cnt = 1

while len(queue) > 1:
    if cnt%2 == 1:
        queue.popleft()
    else:
        queue.append(queue.popleft())
    cnt += 1

print(queue.pop())