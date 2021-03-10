#Challenge - Write a program to find greatest common diviser (GCD) or highest common factor (HCF) of given two numbers.
firstNo = int(input("Enter first number : "))
secondNo = int(input("Enter second number : "))
if firstNo > secondNo:
    val = firstNo
else:
    val = secondNo
for i in range(1,val):
    if firstNo % i == 0 and secondNo % i == 0:
        hcf = i
print(hcf)
