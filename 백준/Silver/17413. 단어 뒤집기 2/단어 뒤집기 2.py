import sys
input = sys.stdin.readline().strip()  # 개행 문자 제거
words = list(input)

is_tag = False
stack = []
new_str = []
for i in words:  
    if i == "<":
        while stack:
            new_str.append(stack.pop())
        is_tag = True
        new_str.append(i)
    elif i == ">":
        new_str.append(i)
        is_tag = False
    elif is_tag:
        new_str.append(i)
    elif not is_tag and i == " ":
        while stack:
            new_str.append(stack.pop())
        new_str.append(i)
    else:
        stack.append(i)

while stack:
    new_str.append(stack.pop())

print("".join(new_str))
