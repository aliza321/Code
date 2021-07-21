def LSS(mat):

    H = [[0 for x in range(Y)] for y in range(X)]
    V = [[0 for x in range(Y)] for y in range(X)]
 
    for i in range(X):
        for j in range(Y):
            if mat[i][j]:
                V[i][j] = (0 if i == 0 else V[i - 1][j]) + 1
                H[i][j] = (0 if j == 0 else H[i][j - 1]) + 1
    max_len = 0
 
    for i in reversed(range(1, X)):
        for j in reversed(range(1, Y)):
 
            l = min(H[i][j], V[i][j])
            while l:
 
                Sq = V[i][j - l + 1] >= l and \
                        H[i - l + 1][j] >= l
                if Sq and max_len < l:
                    max_len = l
                    l = l - 1
    return max_len
 
 
if __name__ == '__main__':
 
    mat = [
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1],
        [0, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 0, 1],
        [1, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 0]
    ]
    (X, Y) = (len(mat), len(mat[0]))
 
    print("The size of the largest square submatrix is", LSS(mat))