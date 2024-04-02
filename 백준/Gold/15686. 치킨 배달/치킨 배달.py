from itertools import combinations

n,m = map(int,input().split())
city = [list(input().split()) for _ in range(n)]
home = []
chicken = []
chicken_distance=[]

def get_chicken_distance(chicken_c):
    sum = 0
    for h in home:
            tmp = []
            for c in chicken_c:
                 sum_tmp = abs(h[0]-c[0])+abs(h[1]-c[1])
                 tmp.append(sum_tmp)
            sum += min(tmp)
    return sum

for i in range(n):
    for j in range(n):
        if city[i][j] == "1":
            home.append([i+1,j+1])
        if city[i][j] == "2":
            chicken.append([i+1,j+1])

for c in combinations(chicken,m):
    chicken_distance.append(get_chicken_distance(c))

print(min(chicken_distance))