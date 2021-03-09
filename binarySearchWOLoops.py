# Challenge - Write the code for binary search without using loops. [optional]

def binarySearch(myList, key):
    start = 0
    end = len(myList)
    while start < end:
        mid = (start + end)//2
        if myList[mid] > key:
            end = mid
        elif myList[mid] < key:
            start = mid + 1
        else:
            return mid
    return -1
 
 
myList = input('Enter the sorted list of numbers: ')
myList = myList.split()
myList = [int(x) for x in myList]
key = int(input('The number to search for: '))
 
index = binarySearch(myList, key)
if index < 0:
    print(f'{key} was not found.')
else:
    print(f'{key} was found at index {index}.')