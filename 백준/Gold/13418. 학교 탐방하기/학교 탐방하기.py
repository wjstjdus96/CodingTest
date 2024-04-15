import sys
input = sys.stdin.readline

def find(parent,p):
    if parent[p] != p:
        parent[p] = find(parent,parent[p])
    return parent[p]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def kruskal():
    parent = [i for i in range(n + 1)]
    tot = 0

    for i in range(m):
        a, b, w = edges[i]
        if find(parent,a) != find(parent,b):
            union(parent,a,b)
            tot += (1 if w == 0 else 0)

    return tot

n, m = map(int, input().split())
edges = [list(map(int, input().split()))for _ in range(m + 1)]

edges.sort(key=lambda x: x[2])
max_distance = kruskal()

edges.sort(key=lambda x: -x[2])
min_distance = kruskal()

print(max_distance ** 2 - min_distance ** 2)