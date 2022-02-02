def fibo(n):
    if( 1 >= n):
        return n
    
    return fibo(n-1) + fibo(n-2)

n = int(input())
print(fibo(n))