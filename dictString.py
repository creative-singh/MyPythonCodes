# Challenge - Write a Python program to create a dictionary from a string.
userVal = input("Enter string to create dictionary : ")
dictionary = {}
for i in userVal:
    if i in dictionary.keys():
        dictionary[i] += 1
    else:
        dictionary[i] = 1
print(dictionary)
