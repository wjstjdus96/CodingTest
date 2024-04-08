from heapq import *
import sys
input = sys.stdin.readline

n, h_centi, t = map(int,input().split())
h_giant = [-int(input()) for _ in range(n)] 
heapify(h_giant)
t_tot = t

while t > 0:
    if -h_giant[0] == 1 or -h_giant[0] < h_centi:
        break
    g = -heappop(h_giant)
    heappush(h_giant,-(g//2))
    t -= 1

if -h_giant[0] < h_centi:
    print("YES")
    print(t_tot - t)
else:
    print("NO")
    print(-h_giant[0])