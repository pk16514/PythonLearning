# Method-1

X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

MatrixSum = []
for i in range(3):
    lst = []
    for j in range(3):
        sum = X[i][j] + Y[i][j]
        lst.append(sum)
    MatrixSum.append(lst)

print(MatrixSum)
print('\r')

# Method-2(List Comprehension)

MatrixSum = [[X[i][j] + Y[i][j] for j in range(3)] for i in range(3)]

print(MatrixSum)
