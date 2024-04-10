import sys
input = sys.stdin.readline

n = int(input())
request = list(map(int,input().split()))
tot_budget = int(input())

if sum(request) <= tot_budget:
    print(max(request))
else:
    start = 1
    end = 100000
    result = 0
    while start <= end:
        mid = (start+end)//2
        sum = 0
        for req in request:
            sum += (req if req<=mid else mid)
        if sum <= tot_budget:
            result = mid
            start = mid+1
        else:
            end = mid-1
    print(result)