n = int(input())
nums = list(map(int,input().split()))
stack = []
answer = [-1]*n

for i in range(n):
    while stack and nums[i] > nums[stack[-1]]:
        idx = stack.pop()
        answer[idx] = nums[i]
    stack.append(i)
print(" ".join(map(str,answer)))