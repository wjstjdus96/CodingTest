n1 = int(input())
arr1 = input().split()
dic = {}

for i in arr1:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

n2 = int(input())
arr2 = input().split()
answer = []

for j in arr2:
    if j in dic.keys():
        answer.append(str(dic[j]))
    else:
        answer.append(str(0))

print(" ".join(answer))