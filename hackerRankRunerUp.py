# Challenge - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    myl = list(arr)
    myl.sort()
    count=0
    myval = max(myl)
    for i in myl:
        if myval == i:
            count+=1
    if count > 1:
        print(myl[len(myl)-count-1])
    else:
        print(myl[len(myl)-2])
