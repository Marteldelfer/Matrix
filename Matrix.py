matrix = [[1, 3, 2],
          [2, 1, 3],
          [2, 3, 1]]

matrix_ = [[2],
           [1],
           [3]]

def determinant(matrix: list):
    """
    Returns determinant of matrix. 
    Parâmeter must be a square matrix, 
    otherwise it wont work properly.
    """
    sum_ = 0
    subt = 0

    for i in range(len(matrix)):
        mult = 1
        mult_subt = 1
        for j in range(len(matrix)):
            mult *= matrix[j][j - i]
            mult_subt *= matrix[j][i - j] 

        sum_ += mult
        subt += mult_subt
    
    return sum_ - subt


def matrix_sum(matrix1: list, matrix2: list):

    new_matrix = [[0 for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            new_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

    return new_matrix

def mult_list(list: list, mult: int):
    return [mult * i for i in list]

def subt_list(list1: list, list2: list):
    return [list1[i] - list2[i] for i in range(len(list1))]

def solve_matrix(matrix1: list, matrix2: list):

    for i in range(len(matrix1)):
        prev_matrix = matrix1
        prev_matrix2 = matrix2
        for j in range(len(matrix)):
            if i != j:
                list1 = mult_list(prev_matrix[j], prev_matrix[i][i])
                list2 = mult_list(prev_matrix[i], prev_matrix[j][i])
                list3 = mult_list(prev_matrix2[j], prev_matrix[i][i])
                list4 = mult_list(prev_matrix2[i], prev_matrix[j][i])

                matrix1[j] = subt_list(list1, list2)
                matrix2[j] = subt_list(list3, list4)
    
    for i in range(len(matrix2)):
        matrix2[i] = mult_list(matrix2[i], 1 / matrix1[i][i])

    return matrix2
                
print(solve_matrix(matrix, matrix_))