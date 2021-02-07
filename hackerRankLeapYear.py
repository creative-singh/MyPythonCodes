# Challenge - To find given year is Leap Year or Not
year = int(input("Enter any year : "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Given Year is Leap Year")
else:
    print("Given Year is not a Leap Year")
