def unlock(myStr):
    myDict = {
        2: ["a", "b", "c"],
        3: ["d", "e", "f"],
        4: ["g", "h", "i"],
        5: ["j", "k", "l"],
        6: ["m", "n", "o"],
        7: ["p", "q", "r", "s"],
        8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"],
    }

    result = ""
    for i in myStr:
        for j in myDict:
            if i.lower() in myDict[j]:
                result += str(j)
                break

    return int(result)


print(unlock("Nokia"))
print(unlock("Valut"))
print(unlock("toilet"))
