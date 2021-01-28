#Challenge :
# Build a very basic login system that takes in input from the username password. checks if username is "Priyesh" and password is "password" and responds with:
#   Username Doesnot Exist
#   Passwords donot match
#   Entered the System

username = input("Your Username : ")
password = input("Your password : ")

if username == "Priyesh" and password == "password":
    print("Entered the System")
elif username == "Priyesh" and password != "password":
    print("Passwords donot match")
elif username != "Priyesh" and password == "password":
    print("Username Doesnot Exist")
else:
    print("Invalid Credential")
     