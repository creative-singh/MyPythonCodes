def square(num):
    string = str(num)
    result = ""
    for i in string:
        result += str(int(i)*int(i))
    return int(result)


print(square(9119))
