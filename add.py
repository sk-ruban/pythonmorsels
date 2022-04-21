def add(*matrices):
    combined = []
    check_shape(matrices)
    for zipped in zip(*matrices):
        new_array = []
        check_shape(zipped)
        for item in zip(*zipped):
            new_array.append(sum(item))
        combined.append(new_array)
    return combined


def check_shape(matrix):
    shape = set()
    for each in matrix:
        shape.add(len(each))
        if len(shape) > 1:
            raise ValueError("Given matrices are not the same size.")


"""
Trey's Solution
def add(*matrices):
    # Add corresponding numbers in given 2-D matrices.
    return [
        # strict checks whether the length of given iterables to zip are of the same length
        [sum(values) for values in zip(*rows, strict=True)]
        for rows in zip(*matrices, strict=True)
    ]
"""

# Base Problem
matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]

# Bonus 1
matrix1 = [[1, 9], [7, 3]]
matrix2 = [[5, -4], [3, 3]]
matrix3 = [[2, 3], [-3, 1]]
add(matrix1, matrix2, matrix3)

# Bonus 2
add([[1, 9], [7, 3]], [[1, 2], [3]])
m1 = [[6, 6], [3, 1]]
m2 = [[1, 2], [3, 4], [5, 6]]
add(m1, m2)