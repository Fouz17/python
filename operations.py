def multiply (matrix1 , matrix2):
    R = len(matrix1)
    C = len(matrix1[0])

    newMatrix = []

    i = 0
    while(i < R):
        j = 0
        newRow = []
        while(j < C):
            n = matrix1[i][j] * matrix2[i][j]
            newRow.append(n)
            j = j + 1
        newMatrix.append(newRow)
        i = i + 1
    k = 0
    print('Multiplied matrix')
    while(k < len(newMatrix)):
        print(newMatrix[k])
        k = k + 1