n = input()
arr = []

for i in range(len(n)):
    arr.append(n[i:i+1])
    for j in range(i+1, len(n)):
        arr.append(n[i:j+1])

print(len(set(arr)))