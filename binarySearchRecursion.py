# Binary Search with Recursion
l=[2,55,2,33,8,55,1]
st,end,find=0,len(l)-1,1
l.sort()
print(l)
def myfunc(l,st,end,find):
    if st > end:
        return "Element Not Found"
    mid = (st+end)//2
    if l[mid] == find:
        return mid
    elif l[mid]<find:
        return myfunc(l,mid+1,end,find)
    else:
        return myfunc(l,st,mid-1,find)
print('Found at index of ',end='')

print(myfunc(l,st,end,find))