import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
edges = []
parent = [i for i in range(n+1)]
tot = 0

for i in range(n):
    for j,cost in enumerate(list(map(int,input().split()))):
        if cost !=0:
            edges.append((cost,i+1,j+1))

edges.sort()

for edge in edges:
    c,a,b = edge
    if find_parent(parent, a) != find_parent(parent,b):
        union_parent(parent,a,b)
        tot += c

print(tot)