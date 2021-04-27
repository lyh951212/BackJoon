import sys

n,x = map(int, input().split())

nums = list(map(int, sys.stdin.readline().split()))

for number in nums:
    if number < x:
        print(number, end=" ")
