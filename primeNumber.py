def primeNumber(num):
    if(num <= 1):
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


num = int(input("Enter a number to check weather its PRIME or NOT: "))
result = primeNumber(num)
if(result):
    print(f"{num} is a PRIME number")
else:
    print(f"{num} is \"NOT\" a PRIME number")
