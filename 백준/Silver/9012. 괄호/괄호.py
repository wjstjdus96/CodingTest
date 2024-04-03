n = int(input())
def check_VPS(s):
    stack = []
    for bracket in s:
        if bracket == "(":
            stack.append(bracket)
        if bracket == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(bracket)
    return "NO" if stack else "YES"

for _ in range(n):
    s = list(input())
    print(check_VPS(s))