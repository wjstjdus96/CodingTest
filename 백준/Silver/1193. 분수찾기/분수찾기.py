n = int(input())
sum,i = 0, 1

while True:
    if (sum + i >= n) :break
    sum += i
    i += 1

left = n - sum
if i % 2 == 0:
    print(str(left)+"/"+str(i+1-left))
else:
    print(str(i+1-left)+"/"+str(left))