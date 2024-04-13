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

n, m = map(int,input().split())
univ = input().split()
parent = [i for i in range(n+1)]
ans, cnt = 0,0
edges = []

for _ in range(m):
    u,v,d = map(int,input().split())
    if univ[u-1] != univ[v-1]:
        edges.append((d,u,v))

edges.sort()

for edge in edges:
    d,u,v = edge
    if find_parent(parent, u) != find_parent(parent, v):
        union_parent(parent,u,v)
        ans += d
        cnt += 1

print(ans if cnt == n-1 else -1)