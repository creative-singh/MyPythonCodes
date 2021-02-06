#Challenge - Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
userVal = int(input("Enter number of last digit in dictionary : "))
d = {}
for i in range(1,userVal):
    d[i]=i*i
print(d)