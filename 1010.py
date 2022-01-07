# 순열 조합 답
#   b개의 지역에 a개의 다리를 놓을 수 있는 경우의 수는 bCa
#   조합은 n개중 r개를 선택하는 경우의 수 중 중복이 없는 것이다.

# def factorial(n):
#     num = 1
#     for i in range(1, n+1):
#         num *= i
#     return num


# T = int(input())

# for _ in range(T):
#     n, m = map(int, input().split())
#     bridge = factorial(m) // (factorial(n) * factorial(m - n))
#     print(bridge)

# ===================================================================

# 다른 답 - 조합의 성질을 이용한 답
import sys
def input():
    return sys.stdin.readline().rstrip()

T = int(input())
dp = [[0 for _ in range(31)] for _ in range(31)]
dp[0][0] = 1
for num in range(1,31):
    dp[num][0] = 1
    for pick in range(1,31):        
        dp[num][pick] = dp[num-1][pick] + dp[num-1][pick-1]
for _ in range(T):
    N,M = map(int,input().split())
    print(dp[M][N])