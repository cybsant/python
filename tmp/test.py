import random

def gen_matrix(rows, cols):
    """Генерация матрицы с заданным размером."""
    matrix = []
    for i in range(int(rows)):
        row = []
        for j in range(int(cols)):
            row.append(random.randint(1, 200))
        matrix.append(row)
    return matrix

def sum_matrix(matrix1, matrix2):
    """Сложение двух матриц."""
    matrix3 = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        matrix3.append(row)
    return matrix3

# Ввод данных
input_str = input("Размер матриц через запятую: ")
rows, cols = input_str.split(',')

matrix1 = gen_matrix(rows, cols)
matrix2 = gen_matrix(rows, cols)
matrix3 = sum_matrix(matrix1, matrix2)

# Выводим результат красиво
print("Матрица №1:")
for row in matrix1:
    print(*row)
print("Матрица №2:")
for row in matrix2:
    print(*row)
print("Сумма матриц:")    
for row in matrix3:
    print(*row)