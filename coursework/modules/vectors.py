"""Модуль с базовыми задачами по векторам."""

import random


def create_and_print_vector() -> list[int]:
    """Создаёт простой вектор и выводит его."""
    vector = [1, 2, 3, 4, 5]
    print("Созданный вектор:", vector)
    return vector


def read_vector_from_keyboard() -> list[int]:
    """Считывает вектор из чисел через пробел."""
    data = input("Введите элементы вектора через пробел: ").split()
    vector = [int(x) for x in data]
    print("Введённый вектор:", vector)
    return vector


def create_random_vector(size: int = 10) -> list[int]:
    """Создаёт вектор из случайных чисел."""
    vector = [random.randint(0, 100) for _ in range(size)]
    print("Случайный вектор:", vector)
    return vector


def random_vector_in_range_and_save(filename: str) -> list[int]:
    """Создаёт случайный вектор в диапазоне пользователя и сохраняет в файл."""
    size = int(input("Размер вектора: "))
    left = int(input("Левая граница диапазона: "))
    right = int(input("Правая граница диапазона: "))

    vector = [random.randint(left, right) for _ in range(size)]
    with open(filename, "a", encoding="utf-8") as file:
        file.write(" ".join(map(str, vector)) + "\n")

    print("Сгенерированный вектор:", vector)
    print(f"Вектор сохранён в {filename}")
    return vector


def max_even_element(vector: list[int]) -> int | None:
    """Ищет максимальный чётный элемент в векторе."""
    even_numbers = [x for x in vector if x % 2 == 0]
    if not even_numbers:
        print("Чётных элементов нет.")
        return None

    result = max(even_numbers)
    print("Максимальный чётный элемент:", result)
    return result
