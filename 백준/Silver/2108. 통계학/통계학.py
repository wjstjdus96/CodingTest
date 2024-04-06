import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]
num.sort()
count = defaultdict(int)
for i in num:
    count[i] += 1
max_count = max(count.values())
max_list = []
for key,val in count.items():
    if val == max_count:
        max_list.append(key)
print(round(sum(num)/n))
print(num[n//2 if n >= 2 else 0])
if len(max_list) == 1:
    print(max_list[0])
else:
    print(sorted(max_list)[1])
print(num[-1]-num[0])