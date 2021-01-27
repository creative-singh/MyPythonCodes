#Challenge :
# Write a program that takes input from the user as marks in 5 subjects and assigns a grade according to the following rules:
# Perc = (s1+s2+s3+s4+s5)/5.
# A, if Perc is 90 or more
# B, if Perc is between 70 and 90(not equal to 90)
# C, if Perc is between 50 and 70(not equal to 90)
# D, if Perc is between 30 and 50(not equal to 90)
# E, if Perc is less than 30

maths = int(input("Enter marks in Maths : "))
english = int(input("Enter marks in English : "))
science = int(input("Enter marks in Science : "))
socialScience = int(input("Enter marks in Social Science : "))
hindi = int(input("Enter marks in Hindi : "))

perc = (maths+english+science+socialScience+hindi)/5

if perc > 100:
    print("Marks are greater than 100")
else:
    if perc >=90:
        print("A")
    elif perc >=70:
        print("B")
    elif perc >=50:
        print("C")
    elif perc >= 30:
        print("D")  
    elif perc <= 30:
        print("E")
         
         
