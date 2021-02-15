# Challenge - https://www.hackerrank.com/challenges/lisa-workbook/problem


def lisaWorkbook(n, k, arr):
    chapter = 0
    page = 0
    problemHi = 0
    problemLow = 0
    specials = 0

    while chapter < len(arr):
        problemLow = problemHi+1
        page += 1

        if problemHi+k > arr[chapter]:
            problemHi = arr[chapter]
        else:
            problemHi += k

        if page <= problemHi and page >= problemLow:
            specials += 1

        if problemHi == arr[chapter]:
            chapter += 1
            problemHi = 0
            problemLow = 0

    return specials
