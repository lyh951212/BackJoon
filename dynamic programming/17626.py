#https://steadily-worked.tistory.com/688

import math

n = int(input()) 

dp = [0 for _ in range(n+1)] 
dp[1] = 1 

for i in range(2, n+1):
    if math.sqrt(i) % 1 == 0: # 결과가 정수다
        dp[i] = 1
        continue
    
    if math.sqrt(i-1) % 1 == 0: # 내값 - 1의 루트가 정수다 
        dp[i] = 2
        continue
    
    temp_min = list()
    for j in range(1 ,math.floor(math.sqrt(i)) + 1):
        if j**2 <= i:
            temp_min.append(dp[i - j**2] + 1)
    
    dp[i] = min(temp_min)
            
print(dp[n])    
        
#==========================================================================
# 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현할 수 있다고 증명하였다
# 합이 결과가 N이 맞는지 판별하지 않아도 됌

# N = int(input())
# dp = [0,1]

# for i in range(2, N+1):
#     min_value = 1e9
#     j = 1

#     while (j**2) <= i:
#         min_value = min(min_value, dp[i - (j**2)])
#         j += 1

#     dp.append(min_value + 1)
# print(dp[N])
    
    