from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())
dic = defaultdict(int)
x = list(map(int,input().split()))

x_set = sorted(set(x))

for idx, num in enumerate(x_set):
    dic[num] = idx

for i in x:
    print(dic[i], end=" ")