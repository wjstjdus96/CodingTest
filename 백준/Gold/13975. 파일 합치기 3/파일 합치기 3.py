from heapq import *
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    size = list(map(int,input().split()))
    tot = 0
    heapify(size)
    while len(size) > 1:
        s1 = heappop(size)
        s2 = heappop(size)
        tot += s1+s2
        heappush(size,s1+s2)
    print(tot)