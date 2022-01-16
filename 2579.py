import sys
n = int(sys.stdin.readline().rstrip())

if n > 300:
    sys.exit()
    
floor = [0 for _ in range(n+2)]
dp = [0 for _ in range(n+2)]
for i in range(n):
    floor[i+1] = int(sys.stdin.readline().rstrip())
    
if sum(floor) > 10000:
    sys.exit()
    
dp_floor_list = [[] for _ in range(n+1)]

dp[1] = floor[1]
dp_floor_list[1].append(1)
        
for i in range(2,n+1):
    invalid_floor = -1
    if i-1 in dp_floor_list[i-1] and i-2 in dp_floor_list[i-1]:
        invalid_floor = i-1
        
    if i-1 in dp_floor_list[i-2] and i-2 in dp_floor_list[i-2]:
        invalid_floor = i-2
    
    if -1 != invalid_floor:
        temp = i-1 if floor[i-1] > floor[i-2] else i-2
        dp[i] = floor[temp] + floor[i]
        dp_floor_list[i].append(temp)
    else:
        dp_idx = i-1 if dp[i-1] > dp[i-2] else i-2
        dp[i] = dp[dp_idx] + floor[i]
        dp_floor_list[i] = dp_floor_list[i] + dp_floor_list[dp_idx]
        
    dp_floor_list[i].append(i)
        

print(dp[n])
