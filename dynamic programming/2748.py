n = int(input())
fibo_list = [0] * (n+1)

fibo_list[0] = 0
fibo_list[1] = 1

a = 2
while(a <= n):
    fibo_list[a] = fibo_list[a-2] + fibo_list[a-1]
    a = a+1

print(fibo_list[n])