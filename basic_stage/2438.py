n= int(input())

#나의 답
# for i in range(1, n+1):
#     for j in range(i):
#         print("*", end = "")
#     print()

#다른 사람  - 파이썬의 장점을 살린 코드
for i in range(1, n+1):
    print("*" * i)