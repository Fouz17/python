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

def matrixMultiply(matrix1,matrix2):
    result = []
    l1 = len(matrix1[0])
    l2 = len(matrix2)

    if l1 == l2:
        x = 0
        while(x < len(matrix1)):
            y = 0
            a = []
            while(y < len(matrix2[0])):
                z = 0
                R = 0
                while(z < len(matrix1[0])):
                    R = R + (matrix1[x][z] * matrix2[z][y])
                    z = z + 1
                a.append(R)
                y = y + 1
            result.append(a)
            x = x + 1
        p = 0
        print('MULTIPLIED MATRIX')
        while(p < len(result)):
            print(result[p])
            p = p + 1
    else:
        print('MATRICES ARE NOT MULTIPLICABLE!')