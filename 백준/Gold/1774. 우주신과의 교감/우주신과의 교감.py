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

def get_distance(d1,d2):
    return ((d1[0]-d2[0])**2 +(d1[1]-d2[1])**2)**0.5

n, m = map(int,input().split())
loc = [(0,0) for _ in range(n+1)]
for i in range(1,n+1):
    x,y = map(int,input().split())
    loc[i] = (x,y)

parent =[i for i in range(n+1)]    
connected = []
edges = []
tot = 0

for i in range(m):
    a,b = map(int,input().split())
    connected.append((a,b))

for c in connected:
    union_parent(parent, c[0], c[1])

for i in range(1,n):
    for j in range(i+1,n+1):
        edges.append((get_distance(loc[i],loc[j]), i,j))

edges.sort()

for edge in edges:
    c,a,b = edge
    if find_parent(parent, a) != find_parent(parent,b):
        union_parent(parent,a,b)
        tot += c

print("%.2f"%(tot))
