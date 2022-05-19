X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

Y_transpose = [[row[i] for row in Y] for i in range(len(Y[0]))]

MatrixMultiplication = []

if(len(X[0]) == len(Y)):
    for row in X:
        lst = []
        for row_ in Y_transpose:
            x = sum([row[i] * row_[i] for i in range(3)])
            lst.append(x)
        MatrixMultiplication.append(lst)

print(MatrixMultiplication)
