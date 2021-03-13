# Given a sorted array of integers A(0 based index) of size N, find the starting and ending position of a given integer B in array A.
# Your algorithm runtime complexity must be in the order of O(log n). Return an array of size 2, such that first element = starting position of B in A and second element = ending position of B in A, if B is not found in A return [-1, -1].
# Input 1:
#     A = [5, 7, 7, 8, 8, 10]
#     B = 8
# Output 1:
#     [3, 4]
# Explanation 1:
#     First occurence of 8 in A is at index 3
#     Second occurence of 8 in A is at index 4
#     ans = [3, 4]
# Input 2:
#     A = [5, 17, 100, 111]
#     B = 3
# Output 2:
#     [-1, -1]


def searchPos(list, target):
  lst = []
  count = 0
  for i in list:
    if i == target:
      lst.append(count)
      count += 1
    else:
      count += 1
  if target not in list:
    return[-1, -1]
  return[min(lst), max(lst)]


num = [2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 7, 8, 9]
n = 5
print(searchPos(num, n))
