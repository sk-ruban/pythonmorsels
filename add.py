# matrix1 = [[1, -2], [-3, 4]]
# matrix2 = [[2, -1], [0, -1]]

matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
matrix3 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]


def add1(*mat):
    newmatrix = []
    for array1, array2 in zip(*mat):
        newarray = []
        for ele1, ele2 in zip(array1, array2):
            newarray.append(ele1 + ele2)
        newmatrix.append(newarray)
    print(newmatrix)

def add(*mat):
    for items in zip(*mat):
        print(items)


add(matrix1, matrix2, matrix3)
