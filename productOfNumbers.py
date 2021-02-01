#Challenge - Take integer inputs from user until he/she presses q (Ask to press q to quit after every integer input).
#           Print average and product of all numbers.
aveCal=0;count=0;productCal=1
while True:
    inpVal = input("Enter number to find Average and Product Or Press \'Q\' to Quit : ")
    if inpVal.isdigit():
        aveCal+=int(inpVal)
        count+=1
        productCal *= int(inpVal)
    elif inpVal == "Q" or inpVal == "q":
        if count == 1:
            print("To find average you have to give 2 numbers")
            print(f"Product of given number is : {productCal}")
            break
        elif count > 1:
            print(f"Average of given no. : {aveCal//count}")
            print(f"Product of given number is : {productCal}")
            break
        else:
            print(f"You Input Irrelevant Value i.e., {b}")
            break
    else:
        print("Input \'Q\' for Quit And Number to find Average and Product")
        break