import sys
input = sys.stdin.readline

n = int(input())
u = sorted([int(input()) for _ in range(n)])
is_continue = True
answer = 0
m = len(u) -1
while is_continue:
    max_target = u[m]
    for i in range(n):
        left = i
        right = n-1
        while left <= right:
            sum = u[i]+u[left]+u[right]
            if sum<max_target: 
                left+=1
            if sum>max_target:
                right-=1
            if sum == max_target:
                answer = max_target 
                is_continue = False
                break
    m -= 1
print(answer)