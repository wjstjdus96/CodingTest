import sys
from heapq import *
input = sys.stdin.readline

n = int(input())
gift = []
for _ in range(n):
    a = input().strip()
    if a == "0":
        print(-heappop(gift) if len(gift) >0 else -1 )
    else:
        charge = a.split()[1:]
        for c in charge:
            heappush(gift,-int(c))