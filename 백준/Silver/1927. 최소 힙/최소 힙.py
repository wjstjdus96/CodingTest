from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    x = int(input())
    if x > 0:
        heappush(arr,x)
    if x == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heappop(arr))