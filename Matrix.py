def mult_list(list: list, mult: int):
    return [mult * i for i in list]

def subt_list(list1: list, list2: list):
    return [list1[i] - list2[i] for i in range(len(list1))]

def print_matrix(m : list[list]) -> None:
    for i in m:
        print(i)

def determinant(matrix: list[list[int]]) -> float:
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


def matrix_sum(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list]:

    new_matrix = [[0 for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            new_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

    return new_matrix

def galsian_elimination(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[float]]:

    for i in range(len(matrix1)):
        prev_matrix = matrix1
        prev_matrix2 = matrix2
        for j in range(len(matrix1)):
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

def inverse_matrix(matrix : list[list]) -> list[list]:
    
    identity = [[0 for i in range(len(matrix))] for i in range(len(matrix))]
    for i in range(len(identity)):
        identity[i][i] = 1
        
    return galsian_elimination(matrix, identity)

def mult_matrix(matrix1 : list[list[int]], matrix2 : list[list[int]]) -> list[list]:

    new_matrix = []
    for line in matrix1:
        new_line = []
        for j in range(len(matrix2)):
            num = 0
            for k in range(len(matrix2)):
                num += line[k] * matrix2[k][j]
            new_line.append(num)
        new_matrix.append(new_line)
    
    return new_matrix

def pow_matrix(matrix : list[list[int]], power : int = 2) -> list[list]:

    new_matrix = matrix
    for i in range(power - 1):
        new_matrix = mult_matrix(new_matrix, matrix)
    return new_matrix