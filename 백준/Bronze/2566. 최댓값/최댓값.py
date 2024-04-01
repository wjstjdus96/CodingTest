arr = []

for _ in range(9):
    n = list(map(int,input().split()))
    for j in range(9):
        arr.append(n[j])

m = max(arr)
idx = [arr.index(m)//9+1, arr.index(m) % 9+1]

print(m)
print(" ".join(map(str,idx)))