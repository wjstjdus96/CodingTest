t = int(input())

for i in range(t):
    n=int(input())
    sticker=[list(map(int,input().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]

    for i in range(n):
        if i==0:
            dp[0][i]=sticker[0][0]
            dp[1][i]=sticker[1][0]
        elif i==1:
            dp[0][i]=dp[1][0]+sticker[0][1]
            dp[1][i]=dp[0][0]+sticker[1][1]
        else:
            dp[0][i]=max(sticker[0][i]+dp[1][i-1], max(dp[0][i-2],dp[1][i-2])+sticker[0][i])
            dp[1][i]=max(sticker[1][i]+dp[0][i-1], max(dp[0][i-2],dp[1][i-2])+sticker[1][i])

    print(max(dp[0][n-1], dp[1][n-1]))