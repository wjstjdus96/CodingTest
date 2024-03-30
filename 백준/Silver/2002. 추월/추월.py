n = int(input())
in_list = []
out_list =[]
inIdx = 0

for _ in range(n):
    in_list.append(input())

for _ in range(n):
    out = input()
    while in_list[inIdx] == "x":
        inIdx += 1
    if in_list[inIdx] == out:
        inIdx +=1
    else:
        in_list[in_list.index(out)] = "x"

print(in_list.count("x"))