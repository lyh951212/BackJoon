#나의 답
import sys
sugar_total = int(sys.stdin.readline())

max_5_cnt = sugar_total // 5
max_3_cnt = sugar_total // 3

result = []

for i in reversed(range(max_5_cnt+1)):
    for j in range(max_3_cnt+1):
        if((5*i + 3*j) > sugar_total):
            break
        if((5*i + 3*j) == sugar_total):
            result.append(i+j) 

if len(result) == 0:
    print(-1)
else:
    print(min(result))

# 더 좋은 답 : https://gabii.tistory.com/entry/BaekJoonPython3-%EB%B0%B1%EC%A4%80-2839%EB%B2%88-%EC%84%A4%ED%83%95%EB%B0%B0%EB%8B%AC
inp = int(input())
Box = 0
while True:
    if (inp % 5) == 0:
        Box = Box + (inp//5)
        print(Box)
        break
    inp = inp-3
    Box += 1
    if inp < 0:
        print("-1")
        break