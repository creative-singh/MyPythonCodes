#Challenge - Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def calStringUpperLower(myval):
    countUpper = 0;countLower = 0;countSpaces = 0
    for i in range(len(myval)):
        if myval[i].islower():
            countLower+=1
        if myval[i].isupper():
            countUpper+=1
        if myval[i].isspace():
            countSpaces+=1
    print(f"Uppercase letters in given string are : {countUpper}")
    print(f"Lowercase letters in given string are : {countLower}")
    print(f"Spaces in given string are : {countSpaces}")
calStringUpperLower(input("Enter any string : "))