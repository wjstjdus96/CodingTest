n = int(input())
tower_list = list(map(int, input().split()))
answer = [0] * n 
stack = [] 

for i in range(n - 1, -1, -1):
    while stack and tower_list[i] >= tower_list[stack[-1]]:
        idx = stack.pop()  
        answer[idx] = i + 1 
    stack.append(i)  

print(" ".join(map(str, answer)))