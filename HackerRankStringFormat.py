#Challenge - Print Decimal , Octal , Hexadecimal(capitalized), Binary
# n=17
n=int(input('Give last value : '))
width = len(bin(n)[2:])
for i in range(1,n+1):
    # print(f'{i}     {oct(i)[2:]}    {str(hex(i)[2:].upper())}    {bin(i)[2:]}')
     print (str(i).rjust(width,' '),str(oct(i)[2:]).rjust(width,' '),str(hex(i)[2:].upper()).rjust(width,' '),str(bin(i)[2:]).rjust(width,' '),sep=' ')
