def counting_sort(arr):

    maximum = max(arr) + 1
    count_arr = [0] * maximum
    sort_arr = [0] * len(arr)

    for i in arr:
        count_arr[i] += 1

    for i in range(1, maximum):
        count_arr[i] += count_arr[i-1]

    for i in arr:
        index = count_arr[i]-1
        sort_arr[index] = i
        count_arr[i] = count_arr[i]-1
    return sort_arr


arr = [4, 2, 2, 8, 3, 3, 1]
sorted_array = counting_sort(arr)
print(sorted_array)
