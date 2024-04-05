import sys
input = sys.stdin.readline

n, m = map(int,input().split())
times = [int(input().strip()) for _ in range(n)]
times.sort()

start = times[0]
end = times[-1]*m
ans = end

while start <= end:
    p_sum = 0
    mid = (start+end)//2
    # 각 심사대에서 mid 시간 동안 처리 가능한 인원수 합 구함
    for time in times:
        p_sum += mid//time
    if p_sum >= m:
        end = mid-1
        ans = min(ans,mid)
    else:
        start = mid+1
print(ans)