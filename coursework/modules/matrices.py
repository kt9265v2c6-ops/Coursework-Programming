"""Модуль с задачами по матрицам."""


def create_matrix_from_vectors(vectors: list[list[int]]) -> list[list[int]]:
    """Создаёт матрицу из списка векторов (строк)."""
    return [row[:] for row in vectors]


def read_matrix_from_file(filename: str) -> list[list[int]]:
    """Читает матрицу из файла, где в строках числа через пробел."""
    matrix = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                matrix.append([int(x) for x in line.split()])
    return matrix


def delete_column_by_index_from_file(matrix: list[list[int]], index_file: str) -> list[list[int]]:
    """Удаляет столбец, индекс которого прочитан из файла."""
    with open(index_file, "r", encoding="utf-8") as file:
        col_index = int(file.read().strip())

    result = []
    for row in matrix:
        if 0 <= col_index < len(row):
            result.append(row[:col_index] + row[col_index + 1 :])
        else:
            result.append(row[:])
    return result


def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """Транспонирует матрицу."""
    return [list(row) for row in zip(*matrix)]


def remove_main_diagonal_one_loop(matrix: list[list[int]]) -> list[list[int]]:
    """Удаляет элементы главной диагонали одним проходом по строкам."""
    result = []
    for i, row in enumerate(matrix):
        new_row = []
        for j, value in enumerate(row):
            if i != j:
                new_row.append(value)
        result.append(new_row)
    return result


def replace_column_from_other_matrix(
    matrix: list[list[int]], other: list[list[int]], column_index: int
) -> list[list[int]]:
    """Заменяет столбец matrix столбцом other."""
    result = [row[:] for row in matrix]
    for i in range(min(len(result), len(other))):
        if column_index < len(result[i]) and column_index < len(other[i]):
            result[i][column_index] = other[i][column_index]
    return result


def zero_row_or_column_by_divisible(matrix: list[list[int]], divisor: int) -> list[list[int]]:
    """Ищет элемент, кратный divisor, и зануляет строку или столбец."""
    result = [row[:] for row in matrix]
    rows = len(result)
    cols = len(result[0]) if rows else 0

    for i in range(rows):
        for j in range(cols):
            if divisor != 0 and result[i][j] % divisor == 0:
                next_value = result[i][j + 1] if j + 1 < cols else 0
                if next_value % 2 == 0:
                    result[i] = [0] * cols
                else:
                    for r in range(rows):
                        result[r][j] = 0
                return result
    return result


def determinant(matrix: list[list[int]]) -> int:
    """Рекурсивно вычисляет детерминант квадратной матрицы."""
    n = len(matrix)
    if n == 0:
        return 0
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(n):
        minor = []
        for row in range(1, n):
            minor.append(matrix[row][:col] + matrix[row][col + 1 :])
        sign = -1 if col % 2 else 1
        det += sign * matrix[0][col] * determinant(minor)
    return det


def multiply_matrices(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    """Умножает матрицы a и b."""
    if not a or not b or len(a[0]) != len(b):
        raise ValueError("Нельзя умножить матрицы: несовместимые размеры")

    rows, cols, common = len(a), len(b[0]), len(b)
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            for k in range(common):
                result[i][j] += a[i][k] * b[k][j]
    return result


def swap_row_with_file_row(
    matrix: list[list[int]], keyboard_row_index: int, row_file: str
) -> list[list[int]]:
    """Меняет местами строку из матрицы со строкой, записанной в файле."""
    with open(row_file, "r", encoding="utf-8") as file:
        file_row = [int(x) for x in file.read().strip().split()]

    result = [row[:] for row in matrix]
    if 0 <= keyboard_row_index < len(result):
        result[keyboard_row_index], file_row = file_row, result[keyboard_row_index]

    with open(row_file, "w", encoding="utf-8") as file:
        file.write(" ".join(map(str, file_row)))

    return result


def print_matrix(matrix: list[list[int]]) -> None:
    """Печатает матрицу построчно."""
    for row in matrix:
        print(" ".join(map(str, row)))
