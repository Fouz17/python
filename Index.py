rows = int(input("ENTER ROW NUMBERS:"))
cols = int(input("ENTER COLUMN NUMBERS:"))
numOfMatrix = int(input("ENTER NUMBER OF MATRIX:"))

matrices = []
#b = []
NOM = 0
while(NOM < numOfMatrix):
    matrix = []
    n = 0
    while (n < rows):
        x = 0
        row = []
        while (x < cols):
            i = int(
                input('ENTER NUMBER OF ROW ' + str(n + 1) + ' COLUMN ' +
                      str(x + 1) + ':'))
            row.append(i)
            x = x + 1
        matrix.append(row)
        n = n + 1
    # print(matrix)
    matrices.append(matrix)
    NOM = NOM + 1
#print(l)

p = 0
while (p < len(matrix)):
    print(matrix[p])
    p = p + 1
print(matrices)

#MADE BY ASAD AND FOUZ AND FAIQ AND ASDULLAH AND AMAN AND QAMBER ALI4
