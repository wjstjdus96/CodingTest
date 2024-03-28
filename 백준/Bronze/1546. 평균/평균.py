n = int(input())
score = list(map(int,input().split()))
m = max(score)

def re_cal(s):
    return s/m*100

score = list(map(re_cal,score))

print(sum(score)/n)