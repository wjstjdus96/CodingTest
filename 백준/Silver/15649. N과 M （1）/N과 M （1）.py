from itertools import permutations

m,n = map(int,input().split())

orders = permutations([i+1 for i in range(m)],n)
for order in orders:
    order = list(map(str,order))
    print(" ".join(order))