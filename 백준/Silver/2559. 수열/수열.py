import sys
input = sys.stdin.readline

n, k = map(int, input().split())
seq = list(map(int,input().split()))

tmp = sum(seq[:k])
max_sum = tmp

for i in range(k, n):
    tmp += seq[i]
    tmp -= seq[i-k]
    if tmp > max_sum:
        max_sum = tmp

print(max_sum)