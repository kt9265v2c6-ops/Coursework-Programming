"""Модуль с операциями над векторами."""

from math import gcd


def reverse_vector(vector: list[int]) -> list[int]:
    """Возвращает вектор в обратном порядке."""
    return vector[::-1]


def sort_vector(vector: list[int], ascending: bool = True) -> list[int]:
    """Сортирует вектор по возрастанию или убыванию."""
    return sorted(vector, reverse=not ascending)


def min_or_max(vector: list[int], find_max: bool) -> int:
    """Ищет минимум или максимум вектора."""
    return max(vector) if find_max else min(vector)


def gcd_of_vector(vector: list[int]) -> int:
    """Находит НОД всех элементов вектора."""
    current_gcd = abs(vector[0])
    for value in vector[1:]:
        current_gcd = gcd(current_gcd, abs(value))
    return current_gcd


def vector_with_smaller_sum(v1: list[int], v2: list[int]) -> list[int]:
    """Возвращает вектор с меньшей суммой элементов."""
    return v1 if sum(v1) <= sum(v2) else v2


def build_vector_from_digits(lines: list[str]) -> list[int]:
    """Из набора строк формирует вектор только из цифр."""
    digits = []
    for line in lines:
        for char in line:
            if char.isdigit():
                digits.append(int(char))
    return digits
