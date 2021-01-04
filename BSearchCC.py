# Challenge - Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
"""
[1,3,5,6], 5 => 2
[1,3,5,6], 2 => 1
[1,3,5,6], 7 => 4
[1,3,5,6], 0 => 0
"""
myList = [1, 3, 5, 6]
target = 0
index = 0

def BSearch(myList, target):
    lowerB = 0
    upperB = len(myList)-1
    while lowerB <= upperB:
        mid = (lowerB+upperB)//2
        if myList[mid] == target:
            globals()['index'] = mid
            return True
        else:
            if myList[mid] < target:
                lowerB = mid+1
            else:
                upperB = mid-1
        globals()['index'] = mid+1
    return False


if BSearch(myList, target):
    print("Found at index of ", index)
else:
    print("Found at imaginary index of ", index)
