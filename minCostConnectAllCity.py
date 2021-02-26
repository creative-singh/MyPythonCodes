def minnode(length, keyval, mstset):
    mini = 999999999999
    min_index = None

    for i in range(length):
        if (mstset[i] is False and
                keyval[i] < mini):
            mini = keyval[i]
            min_index = i
    return min_index


def findcost(length, city):

    parent = [None] * length
    keyval = [None] * length

    mstset = [None] * length

    for i in range(length):
        keyval[i] = 9999999999999
        mstset[i] = False

    parent[0] = -1
    keyval[0] = 0
    for i in range(length - 1):

        u = minnode(length, keyval, mstset)
        mstset[u] = True
        for v in range(length):
            if (city[u][v] and mstset[v] is False and
                    city[u][v] < keyval[v]):
                keyval[v] = city[u][v]
                parent[v] = u

    cost = 0
    for i in range(1, length):
        cost += city[parent[i]][i]
    print(cost)


city = [[0, 1, 2, 3, 4],
        [1, 0, 5, 0, 7],
        [2, 5, 0, 6, 0],
        [3, 0, 6, 0, 0],
        [4, 7, 0, 0, 0]]
length = len(city)
findcost(length, city)
