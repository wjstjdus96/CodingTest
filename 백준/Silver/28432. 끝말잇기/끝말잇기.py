n1 = int(input())
words = []

for _ in range(n1):
    words.append(input())

idx = words.index("?")
first = words[idx-1][-1] if 1 <= idx else ""
last = words[idx+1][0] if idx <= len(words) - 2 else ""

n2 = int(input())
for _ in range(n2):
    example = input()
    if(example in words):
        continue
    if(len(words) == 1):
        print(example)
        break
    if(idx == 0):
        if(example[-1] == last):
            print(example)
            break
    if(idx == len(words) -1):
        if(example[0] == first):
            print(example)
            break
    if(idx != 0 and idx != len(words) -1):
        if(example[0] == first and example[-1] == last):
            print(example)
            break