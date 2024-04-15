from collections import deque
import sys
input = sys.stdin.readline

def bfs(n):
    queue = deque([(n, 0)]) 
    visited = set()

    while queue:
        num, count = queue.popleft()
        if num == 1:
            return count
        if num % 3 == 0 and num // 3 not in visited:
            queue.append((num // 3, count + 1))
            visited.add(num // 3)
        if num % 2 == 0 and num // 2 not in visited:
            queue.append((num // 2, count + 1))
            visited.add(num // 2)
        if num - 1 not in visited:
            queue.append((num - 1, count + 1))
            visited.add(num - 1)

n = int(input())
print(bfs(n))