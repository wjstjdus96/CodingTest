import sys
input = sys.stdin.readline

n = int(input())
stack=[]
stack_num = 1
cal = []

for _ in range(n):
    num = int(input())
    while stack_num <= num:
        stack.append(stack_num)
        cal.append("+")
        stack_num+=1
    if stack[-1] == num:
        stack.pop()
        cal.append("-")
    else:
        cal = []
        cal.append("NO")
        break
print("\n".join(cal))