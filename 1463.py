n = int(input())
dp = [0 for _ in range(1000000+1)]
dp[2] = 1
dp[3] = 1

for i in range(4, n+1):
    dp[i]  = dp[i-1] + 1
    if 0 == i % 3:
        dp[i]  = min(dp[i], dp[i//3] + 1)
    if 0 == i % 2:
        dp[i]  = min(dp[i], dp[i//2] + 1)
        
print(dp[n]) 
        