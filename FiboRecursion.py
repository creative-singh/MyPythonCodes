def fib(a,b,n):
    if n == 0:
        return 
    result=a+b
    print(result)
    fib(b,result,n-1)
i,j = 0,1
n=int(input())
print(i)
print(j)
fib(i,j,n-2)