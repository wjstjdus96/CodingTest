from heapq import *

n, m = map(int,input().split())
a = list(map(int,input().split()))
heapify(a)

for _ in range(m):
    a1, a2 = heappop(a), heappop(a)
    sum_a = a1 + a2
    heappush(a, sum_a)
    heappush(a, sum_a)
    
print(sum(a))