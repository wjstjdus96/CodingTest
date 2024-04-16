n = int(input())
k = int(input())
sensor = list(map(int,input().split()))
dist = []

if n <= k:
    print(0)
else:
    sensor.sort()
    for i in range(0,n-1):
        dist.append(sensor[i+1]-sensor[i])

    dist.sort()
    for _ in range(k-1):
        dist.pop()

    print(sum(dist))