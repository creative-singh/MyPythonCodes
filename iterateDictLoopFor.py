# Challenge - Write a Python program to iterate over dictionaries using for loops .
mydict = {"Hello": "use as a greeting", "Proud": "feeling deep pleasure",
          "Programmer": "person who is mentally unstable"}
for i in mydict:
    print(f"{i} - {mydict.get(i)}")
