N, S = map(int, input().split())
num = list(map(int, input().split()))

min_length = N+1
left = 0
right = 0
sub_total = 0

while right < N:
    sub_total += num[right]
    
    while sub_total >= S:
        min_length = min(min_length, right - left + 1)
        sub_total -= num[left]
        left += 1
    
    right += 1

print(min_length if min_length != N+1 else 0)