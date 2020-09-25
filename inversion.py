def inversion(myList, n): 
    count = 0
    for i in range(n):
        for j in range(i + 1, n): 
            if (myList[i] > myList[j]): 
                count += 1
  
    return count 
  
myList = [1, 20, 6, 4, 5] 
n = len(myList) 
print(inversion(myList, n))