n = int(input())
dic = {}

for _ in range(n):
    [fruit, i] = input().split()
    if fruit in dic.keys():
        dic[fruit] += int(i)
    else:
        dic[fruit] = int(i)

print("YES" if 5 in dic.values() else "NO")