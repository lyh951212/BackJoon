import sys

n = int(sys.stdin.readline().rstrip())

if n > 300 or n <= 0:
    sys.exit()
    
floor   = [0 for _ in range(301)]
dp      = [0 for _ in range(301)]
for i in range(n):
    floor[i+1] = int(sys.stdin.readline().rstrip())
    if floor[i+1] > 10000:
        sys.exit()

dp_floor_list = [[] for _ in range(n+1)]
dp[1] = floor[1]
dp[2] = floor[1] + floor[2]
dp[3] = max(floor[1] + floor[3], floor[2] + floor[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-3] + floor[i-1] + floor[i], dp[i-2] + floor[i])
print(dp[n])
