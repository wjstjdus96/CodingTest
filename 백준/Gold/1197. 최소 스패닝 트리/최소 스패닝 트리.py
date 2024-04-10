# 부모 노드를 반환
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 최상위 부모를 찾은 뒤 부모노드 조정
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int,input().split())
edges = []
tot = 0
parent = [i for i in range(v+1)] # 부모테이블 초기화

for _ in range(e):
    a,b,c = map(int, input().split())
    edges.append((c,a,b))
edges.sort()

for edge in edges:
    c,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        tot += c

print(tot)