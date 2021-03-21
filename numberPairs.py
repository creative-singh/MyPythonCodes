# Challenge - https://www.geeksforgeeks.org/find-number-pairs-xy-yx/


def num_of_pairs(x, y):
  i_count = 0
  for i in range(len(x)):
    for j in range(len(y)):
      if pow(x[i], y[j]) > pow(y[j], x[i]):
        i_count += 1
  return i_count


list1 = [2, 1, 6]
list2 = [1, 5]
print(num_of_pairs(list1, list2))
