import math
import sys
input = sys.stdin.readline

def cal_distance(x1,x2,y1,y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
edges=[]
stars = []
parent = [i for i in range(n+1)]
tot = 0

for _ in range(n):
    x,y = map(float,input().split())
    stars.append((x,y))

for i in range(len(stars)):
    for j in range(i+1,len(stars)):
        edge = cal_distance(stars[i][0],stars[j][0],stars[i][1],stars[j][1])
        edges.append((edge,i,j))
edges.sort()

for edge in edges:
    cost, s1, s2 = edge
    if find_parent(parent,s1) != find_parent(parent, s2):
        union_parent(parent, s1,s2)
        tot += cost

print(round(tot,2))