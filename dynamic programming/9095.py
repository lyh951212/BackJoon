
# import itertools
# import sys

# test_case_cnt = int(input())
# test_case = list()

# for _ in range(test_case_cnt):
#     n = int(input()) 
#     permu_list = list()
#     for i in range(2, n+1):
#         permu_list.append(list(itertools.product([1,2,3], repeat=i)))


#     result = 0 
#     for permu in permu_list:
#         for data in permu:
#             if n == sum(data):
#                 result = result +1
#     print(result)

#https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-9095%EB%B2%88-1-2-3-%EB%8D%94%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython
import sys

def input():
    return sys.stdin.readline().rstrip()

tc = int(input())

dp = [0] * 15
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 12):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

for _ in range(tc):
    n = int(input())

    print(dp[n])