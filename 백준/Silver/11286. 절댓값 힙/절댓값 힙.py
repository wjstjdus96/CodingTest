from heapq import *
import sys

input = sys.stdin.readline
n = int(input())
h = []

for _ in range(n):
    x = int(input())
    if x != 0:
        t = (abs(x),x)
        heappush(h,t)
    if x == 0:
        if len(h) == 0:
            print(0)
        else:
            print(heappop(h)[1])
