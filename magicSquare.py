#Challenge - https://www.hackerrank.com/challenges/magic-square-forming/problem


def formingMagicSquare(s):
    magic = [
            [8, 1, 6, 3, 5, 7, 4, 9, 2],
            [6, 1, 8, 7, 5, 3, 2, 9, 4],
            [4, 9, 2, 3, 5, 7, 8, 1, 6],
            [2, 9, 4, 7, 5, 3, 6, 1, 8],
            [8, 3, 4, 1, 5, 9, 6, 7, 2],
            [4, 3, 8, 9, 5, 1, 2, 7, 6],
            [6, 7, 2, 1, 5, 9, 8, 3, 4],
            [2, 7, 6, 9, 5, 1, 4, 3, 8],
    ]
    s_list = [j for sub in s for j in sub]
    cost_list = []
    for i in magic:
        cost_sum = 0
        for j in range(9):
            cost_sum += abs(i[j]-s_list[j])
        cost_list.append(cost_sum)

    return min(cost_list)
