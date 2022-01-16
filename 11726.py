import sys

def Input():
    return sys.stdin.readline().rstrip()

n = int(Input())
if n > 1000 or n < 1:
    sys.exit()
    
dp = [0 for _ in range(n+2)]

dp[1] = 1
dp[2] = 2
for i in range(3, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n]%10007)

#런타임 에러
# dp = [0 for _ in range(n+1)] 로 하면 n=1일때 런타임에러 남