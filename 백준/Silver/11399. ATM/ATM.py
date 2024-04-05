n = int(input())
per = list(map(int,input().split()))
per.sort()
answer = 0

for idx, time in enumerate(per):
    left = n-(idx+1)
    answer += (time + left*time)

print(answer)