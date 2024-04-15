import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n = int(input())
edges = []
parent = [i for i in range(n+1)]
cnt = 0
tot = 0
lng = 0

for i in range(n):
    lst = list(input())
    for j in range(n):
        if 'a' <= lst[j] <= 'z':
            edges.append((ord(lst[j])-ord('a')+1,i,j))
            tot += ord(lst[j])-ord('a')+1
        if "A" <= lst[j] <= "Z":
            edges.append((ord(lst[j])-ord('A')+27,i,j))
            tot += ord(lst[j])-ord('A')+27

edges.sort()

for edge in edges:
    c, a,b = edge
    if find(a) != find(b):
        union(a, b)
        lng += c
        cnt += 1

print(tot-lng if cnt == n-1 else -1)