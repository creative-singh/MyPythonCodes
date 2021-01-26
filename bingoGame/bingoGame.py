def bingo(arr):
    bing = [2, 7, 9, 14, 15]
    for i in arr:
        if (i in bing):
            remove = bing.index(i)
            bing.pop(remove)
    if len(bing) == 0:
        return "WIN"
    else:
        return "LOSE"


print(bingo([21, 13, 2, 7, 5, 14, 7, 15, 9, 10]))  # "WIN"
print(bingo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))      # "LOSE"
