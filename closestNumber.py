#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    pair = []
    minDiff = 20000001

    for i in range(n-1):
        diff = abs(arr[i] - arr[i+1])
        if diff < minDiff:
            pair = [arr[i], arr[i+1]]
            minDiff = diff
        elif diff == minDiff:
            pair.extend(arr[i])
            pair.extend(arr[i+1])
    return(pair)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
