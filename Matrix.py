matrix = [[1, 3, 2],
          [2, 1, 3],
          [2, 3, 1]]

def determinant(matrix: list):
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
    
print(determinant(matrix))
