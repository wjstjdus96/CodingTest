n = int(input())
table = []

for _ in range(n):
    table += list(map(int,input().split()))
    table = sorted(table,reverse=True)[:n]
print(table[-1])    