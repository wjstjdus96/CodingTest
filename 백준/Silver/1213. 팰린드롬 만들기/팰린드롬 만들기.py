n = input()
dic = {}
arr = []
oneChar = []

for i in n:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for char,num in dic.items():
    if num % 2 == 1:
        oneChar.append(char)
        num -= 1
    if num != 0 and num % 2 == 0:
        arr += [char]*(num//2)

if len(oneChar) > 1:
    print("I'm Sorry Hansoo")
else:        
    side = "".join(sorted(arr))
    center = oneChar[0] if len(oneChar) == 1 else ""
    print(side + center + side[::-1])