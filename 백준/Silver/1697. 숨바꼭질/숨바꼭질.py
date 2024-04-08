from collections import deque
import sys
input=sys.stdin.readline

n,k=map(int,input().split())
max_num=100000
visited=[0]*(max_num+1)

def bfs(n):
  q=deque()
  q.append(n)
  global k
  
  while q:
    x=q.popleft()
    if x==k:
      return visited[x]
    for i in (x-1,x+1,x*2):
      if 0<=i<=max_num and visited[i]==0:
        visited[i]=visited[x]+1
        q.append(i)

print(bfs(n))