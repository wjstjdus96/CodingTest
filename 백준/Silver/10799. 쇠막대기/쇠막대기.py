import sys
input = sys.stdin.readline

stack = []
cnt = 0
sum = 0

for bracket in list(input()):
    if bracket == "(":
        stack.append(bracket)
        cnt += 1
    if bracket == ")":
        if stack and stack[-1] == "(":
            cnt -= 1
            sum += cnt
            stack.pop()
            stack.append("r")
        else:
            cnt -= 1
            sum += 1
print(sum)