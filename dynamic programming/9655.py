# 홀수일 때는 SK가 이기고 짝수일 때는 항상 CY가 이긴다
# https://claude-u.tistory.com/325
n = int(input())
if n % 2 == 0:
    print('CY')
else:
    print('SK')
    
# ==============================================================

# dp로 푼 문제
# 홀수일 때는 SK가 이기고 짝수일 때는 항상 CY가 이긴다
import sys
def input():
    return sys.stdin.readline().rstrip()

dp = ['' for _ in range(1001)]
dp[1] = 'SK'

for i in range(1,1000):
    if dp[i]=="SK":
        if dp[i+1]=='':
            dp[i+1] = 'CY'
        if i+3<1000:
            dp[i+3] = 'CY'
    elif dp[i]=='CY':
        if dp[i+1]=='':
            dp[i+1] = 'SK'
        if i+3<1000:
            dp[i+3] = 'SK'

print(dp[int(input())]) 
