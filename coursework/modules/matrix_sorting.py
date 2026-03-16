"""Модуль с алгоритмами сортировки для матриц."""


def _flatten(matrix: list[list[int]]) -> list[int]:
    return [item for row in matrix for item in row]


def _restore(flat: list[int], rows: int, cols: int) -> list[list[int]]:
    return [flat[i * cols : (i + 1) * cols] for i in range(rows)]


def shell_sort(data: list[int]) -> list[int]:
    arr = data[:]
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


def bubble_sort(data: list[int]) -> list[int]:
    arr = data[:]
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(data: list[int]) -> list[int]:
    arr = data[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(data: list[int]) -> list[int]:
    arr = data[:]
    n = len(arr)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr


def heap_sort(data: list[int]) -> list[int]:
    arr = data[:]

    def heapify(n: int, i: int) -> None:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)
    return arr


def sort_matrix_elements(matrix: list[list[int]], method: str) -> list[list[int]]:
    """Сортирует все элементы матрицы выбранным методом."""
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    flat = _flatten(matrix)

    methods = {
        "shell": shell_sort,
        "bubble": bubble_sort,
        "insertion": insertion_sort,
        "selection": selection_sort,
        "heap": heap_sort,
    }

    if method not in methods:
        raise ValueError("Неизвестный метод сортировки")

    sorted_flat = methods[method](flat)
    return _restore(sorted_flat, rows, cols)
