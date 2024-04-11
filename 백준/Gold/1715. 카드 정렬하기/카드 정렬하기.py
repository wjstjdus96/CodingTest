from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]
heapify(cards)
tot = 0

while len(cards) > 1:
    c1 = heappop(cards)
    c2 = heappop(cards)
    tot += c1+c2
    heappush(cards, c1+c2)

print(tot)

