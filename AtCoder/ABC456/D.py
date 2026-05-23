S = str(input())

dp = [[0] * 3 for _ in range(len(S))]

for i in range(len(S)):
    if S[i] != "a":
        dp[i][0] = dp[i - 1][0] % 998244353
    else:
        dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 998244353



