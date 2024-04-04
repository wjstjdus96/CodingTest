from collections import defaultdict
n = int(input())

def get_clothes(d):
    sum = 1
    for _, val in d.items():
        sum *= (val+1)
    return sum -1

for _ in range(n):
    dict = defaultdict(int)
    for _ in range(int(input())):
        _, type = input().split()
        dict[type] += 1
    print(get_clothes(dict))