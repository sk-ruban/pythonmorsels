# matrix1 = [[1, -2], [-3, 4]]
# matrix2 = [[2, -1], [0, -1]]

matrix1 = [[1, 9], [7, 3]]
matrix2 = [[5, -4], [3, 3]]
matrix3 = [[2, 3], [-3, 1]]


def add(*mat):
    newmatrix = []
    for zipped in zip(*mat):
        newarray = []
        for ele in zip(*zipped):
            newarray.append(sum(ele))
        newmatrix.append(newarray)
    print(newmatrix)


add(matrix1, matrix2, matrix3)
