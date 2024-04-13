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

n,m,k = map(int,input().split())
installed = list(map(int,input().split()))
parent = [i for i in range(n+1)]
edges = []
ans = 0

for i in range(len(installed)-1):
    union_parent(parent, installed[i], installed[i+1])

for i in range(m):
    u,v,c = map(int,input().split())
    edges.append((c,u,v))

edges.sort()

for edge in edges:
    c,u,v = edge
    if find_parent(parent,u) != find_parent(parent,v):
        union_parent(parent,u,v)
        ans += c

print(ans)