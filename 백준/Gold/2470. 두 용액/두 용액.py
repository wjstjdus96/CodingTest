n = int(input())
sol = sorted(list(map(int,input().split())))


sol_left = sol[-1]
sol_right = sol[0]
min_sum = max(abs(sol_left),abs(sol_right))*2

for i in range(n):
    left, right = i+1, n-1
    while left <= right:
        mid = (left+right)//2
        cur_sum = sol[i] + sol[mid]
        if abs(cur_sum) < min_sum:
            min_sum = abs(cur_sum)
            sol_left = sol[i]
            sol_right = sol[mid]
        if cur_sum == 0:
            break
        elif cur_sum < 0:
            left = mid+1
        else:
            right = mid-1

print(sol_left,sol_right)