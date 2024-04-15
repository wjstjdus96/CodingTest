from collections import deque

n,w,l = map(int,input().split())
trucks = deque(list(map(int,input().split())))

tot_weight = 0
bridge = deque([0 for _ in range(w)])
time = 0
while True:
    tot_weight -= bridge.popleft()
    if trucks:
        if tot_weight+trucks[0] <= l:
            new = trucks.popleft()
            bridge.append(new)
            tot_weight += new
        else:
            bridge.append(0)
    time += 1
    if tot_weight == 0: 
        break

print(time)
