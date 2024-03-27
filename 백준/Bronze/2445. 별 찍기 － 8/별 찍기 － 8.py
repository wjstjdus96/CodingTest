n = int(input())

for i in range(1, n):
    for j in range(1, 2*n+1):
        if(j <= i or 2*n-i < j):
            print("*",end="")
        else:
            print(" ",end="")
    print("")

for i in range(n, 0, -1):
    for j in range(1, 2*n+1):
        if(j <= i or 2*n-i < j):
            print("*",end="")
        else:
            print(" ",end="")
    print("")