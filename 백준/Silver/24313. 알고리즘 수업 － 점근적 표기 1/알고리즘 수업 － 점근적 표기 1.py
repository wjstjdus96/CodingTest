a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())

def fn(n):
    return a1*n + a0 <= c*n

if fn(n0) and a1 <= c:
    print(1)
else:
    print(0)