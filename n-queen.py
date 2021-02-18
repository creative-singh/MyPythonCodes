N = int(input('Board size: '))
board = [[0]*N for x in range(N)]


def is_attacked(row, col):
    for i in range(0, N):
        if board[row][i] == 1 or board[i][col] == 1:
            return True

    for i in range(0, N):
        for j in range(0, N):
            if((row+col) == (i+j)) or ((row-col) == (i-j)):
                if board[i][j] == 1:
                    return True
    return False


def n_queen(n):

    if n == 0:
        return True
    for i in range(0, N):
        for j in range(0, N):
            if (not is_attacked(i, j)) and (board[i][j] != 1):
                board[i][j] = 1
                if n_queen(n-1) == True:
                    return True
                board[i][j] = 0
    return False


if n_queen(N) == False:
    print("Not possible")
else:
    for i in range(N):
           for j in range(N):
                print(board[i][j], end=" ")
            print()