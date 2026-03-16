"""Главная программа курсовой: текстовое меню для всех задач."""

from modules import file_operations, graphics, matrices, matrix_sorting, string_processing, vector_operations, vectors

DATA_MATRIX = "data/sample_matrix.txt"
DATA_TEXT = "data/sample_text.txt"
TEMP_INDEX = "data/column_index.txt"
TEMP_ROW = "data/swap_row.txt"


def input_int(message: str) -> int:
    """Безопасный ввод целого числа."""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Ошибка: введите целое число.")


def input_vector() -> list[int]:
    """Безопасный ввод вектора."""
    while True:
        try:
            return [int(x) for x in input("Введите элементы через пробел: ").split()]
        except ValueError:
            print("Ошибка: используйте только целые числа.")


def print_menu(title: str, items: list[str]) -> None:
    print(f"\n=== {title} ===")
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")
    print("0. Назад")


def file_menu() -> None:
    while True:
        print_menu("Работа с файлами", [
            "Считать с клавиатуры и вывести",
            "Считать с клавиатуры и записать в файл",
            "Считать из файла и вывести",
            "Считать с клавиатуры и записать в начало файла",
        ])
        choice = input("Выбор: ")

        if choice == "1":
            file_operations.read_keyboard_and_print()
        elif choice == "2":
            file_operations.read_keyboard_and_write_to_file(DATA_TEXT)
        elif choice == "3":
            file_operations.read_file_and_print(DATA_TEXT)
        elif choice == "4":
            file_operations.write_to_file_start(DATA_TEXT)
        elif choice == "0":
            return
        else:
            print("Неизвестный пункт меню.")


def vectors_menu() -> None:
    current_vector = [2, 4, 5, 8, 11]

    while True:
        print_menu("Векторы", [
            "Создать вектор и вывести",
            "Считать вектор с клавиатуры",
            "Создать случайный вектор",
            "Создать случайный вектор в диапазоне и записать в файл",
            "Найти максимальный среди чётных",
        ])
        choice = input("Выбор: ")

        if choice == "1":
            current_vector = vectors.create_and_print_vector()
        elif choice == "2":
            current_vector = vectors.read_vector_from_keyboard()
        elif choice == "3":
            size = input_int("Размер вектора: ")
            current_vector = vectors.create_random_vector(size)
        elif choice == "4":
            current_vector = vectors.random_vector_in_range_and_save(DATA_TEXT)
        elif choice == "5":
            vectors.max_even_element(current_vector)
        elif choice == "0":
            return
        else:
            print("Неизвестный пункт меню.")


def vector_operations_menu() -> None:
    while True:
        print_menu("Операции с векторами", [
            "Вывести вектор в обратной последовательности",
            "Отсортировать вектор по возрастанию/убыванию",
            "Найти минимум/максимум",
            "Найти НОД элементов вектора",
            "Сравнить суммы двух векторов",
            "Сформировать вектор из цифр строк",
        ])
        choice = input("Выбор: ")

        if choice == "1":
            vector = input_vector()
            print(vector_operations.reverse_vector(vector))
        elif choice == "2":
            vector = input_vector()
            key = input("Введите 'asc' или 'desc': ").strip().lower()
            print(vector_operations.sort_vector(vector, ascending=(key != "desc")))
        elif choice == "3":
            vector = input_vector()
            key = input("Введите 'min' или 'max': ").strip().lower()
            print(vector_operations.min_or_max(vector, find_max=(key == "max")))
        elif choice == "4":
            vector = input_vector()
            print("НОД:", vector_operations.gcd_of_vector(vector))
        elif choice == "5":
            print("Первый вектор:")
            v1 = input_vector()
            print("Второй вектор:")
            v2 = input_vector()
            print("Вектор с меньшей суммой:", vector_operations.vector_with_smaller_sum(v1, v2))
        elif choice == "6":
            count = input_int("Сколько строк ввести: ")
            lines = [input(f"Строка {i + 1}: ") for i in range(count)]
            print("Вектор цифр:", vector_operations.build_vector_from_digits(lines))
        elif choice == "0":
            return
        else:
            print("Неизвестный пункт меню.")


def matrix_menu() -> None:
    while True:
        print_menu("Матрицы", [
            "Создать матрицу из нескольких векторов",
            "Удалить столбец по индексу из файла",
            "Транспонировать матрицу",
            "Удалить главную диагональ",
            "Заменить столбец матрицы столбцом из другой матрицы",
            "Найти элемент кратный числу и занулить строку/столбец",
            "Найти детерминант матрицы",
            "Умножить матрицу из файла на матрицу с клавиатуры",
            "Поменять местами строку с данными из файла",
        ])
        choice = input("Выбор: ")

        if choice == "1":
            rows = input_int("Количество строк: ")
            vectors_data = []
            for i in range(rows):
                print(f"Строка {i + 1}:")
                vectors_data.append(input_vector())
            matrices.print_matrix(matrices.create_matrix_from_vectors(vectors_data))
        elif choice == "2":
            matrix = matrices.read_matrix_from_file(DATA_MATRIX)
            index = input_int("Введите индекс столбца (запишется в файл): ")
            with open(TEMP_INDEX, "w", encoding="utf-8") as f:
                f.write(str(index))
            matrices.print_matrix(matrices.delete_column_by_index_from_file(matrix, TEMP_INDEX))
        elif choice == "3":
            matrix = matrices.read_matrix_from_file(DATA_MATRIX)
            matrices.print_matrix(matrices.transpose_matrix(matrix))
        elif choice == "4":
            matrix = matrices.read_matrix_from_file(DATA_MATRIX)
            matrices.print_matrix(matrices.remove_main_diagonal_one_loop(matrix))
        elif choice == "5":
            print("Первая матрица (из файла):")
            matrix = matrices.read_matrix_from_file(DATA_MATRIX)
            rows = len(matrix)
            print(f"Введите вторую матрицу ({rows} строк):")
            other = [input_vector() for _ in range(rows)]
            col = input_int("Номер столбца: ")
            matrices.print_matrix(matrices.replace_column_from_other_matrix(matrix, other, col))
        elif choice == "6":
            matrix = matrices.read_matrix_from_file(DATA_MATRIX)
            divisor = input_int("Введите число: ")
            matrices.print_matrix(matrices.zero_row_or_column_by_divisible(matrix, divisor))
        elif choice == "7":
            matrix = matrices.read_matrix_from_file(DATA_MATRIX)
            if len(matrix) == len(matrix[0]):
                print("Детерминант:", matrices.determinant(matrix))
            else:
                print("Матрица не квадратная.")
        elif choice == "8":
            a = matrices.read_matrix_from_file(DATA_MATRIX)
            print(f"Введите матрицу B из {len(a[0])} строк:")
            b = [input_vector() for _ in range(len(a[0]))]
            try:
                matrices.print_matrix(matrices.multiply_matrices(a, b))
            except ValueError as error:
                print(error)
        elif choice == "9":
            matrix = matrices.read_matrix_from_file(DATA_MATRIX)
            row = input_int("Какую строку матрицы заменить: ")
            with open(TEMP_ROW, "w", encoding="utf-8") as f:
                f.write("9 9 9")
            matrices.print_matrix(matrices.swap_row_with_file_row(matrix, row, TEMP_ROW))
        elif choice == "0":
            return
        else:
            print("Неизвестный пункт меню.")


def sorting_menu() -> None:
    methods = ["shell", "bubble", "insertion", "selection", "heap"]

    while True:
        print_menu("Сортировки матриц", [
            "Сортировка методом Шелла",
            "Пузырьковая сортировка",
            "Сортировка вставками",
            "Сортировка выбором",
            "Сортировка кучей",
        ])
        choice = input("Выбор: ")

        if choice in {"1", "2", "3", "4", "5"}:
            matrix = matrices.read_matrix_from_file(DATA_MATRIX)
            method = methods[int(choice) - 1]
            result = matrix_sorting.sort_matrix_elements(matrix, method)
            matrices.print_matrix(result)
        elif choice == "0":
            return
        else:
            print("Неизвестный пункт меню.")


def string_menu() -> None:
    while True:
        print_menu("Строки", [
            "Вывести форматированный текст",
            "Вывести таблицу псевдографикой",
            "Удалить символы из строки файла",
            "Поиск подстроки в файле (неполное совпадение)",
            "Вывести слова нечётной длины из файла",
        ])
        choice = input("Выбор: ")

        if choice == "1":
            text = input("Введите текст: ")
            left, center, right = string_processing.format_text(text)
            print("Левый край :", left)
            print("Центр      :", center)
            print("Правый край:", right)
        elif choice == "2":
            rows = input_int("Строк в таблице: ")
            cols = input_int("Столбцов в таблице: ")
            print(string_processing.draw_ascii_table(rows, cols))
        elif choice == "3":
            chars = input("Какие символы удалить: ")
            print(string_processing.remove_chars_from_file_line(DATA_TEXT, chars))
        elif choice == "4":
            query = input("Введите строку для поиска: ")
            line_no = string_processing.search_partial_in_file(DATA_TEXT, query)
            print("Последний номер строки:", line_no)
        elif choice == "5":
            words = string_processing.odd_length_words_from_file(DATA_TEXT)
            print("Слова нечётной длины:", words)
        elif choice == "0":
            return
        else:
            print("Неизвестный пункт меню.")


def graphics_menu() -> None:
    while True:
        print_menu("Графика Tkinter", [
            "Нарисовать квадрат",
            "Вписать треугольник в круг",
            "Наложить на треугольник круг радиуса R/4",
            "Построить гистограмму по вектору",
            "Матрица с выделением min и max",
            "Матрица из файла, раскраска строк",
            "Матрица из файла, раскраска столбцов",
            "Отсортированная матрица с градиентом строк",
        ])
        choice = input("Выбор: ")

        if choice == "1":
            graphics.draw_square()
        elif choice == "2":
            graphics.triangle_in_circle(input_int("Радиус: "))
        elif choice == "3":
            graphics.overlay_small_circle_on_triangle(input_int("Радиус: "))
        elif choice == "4":
            vector = input_vector()
            graphics.draw_histogram(vector)
        elif choice == "5":
            matrix = matrices.read_matrix_from_file(DATA_MATRIX)
            graphics.draw_matrix_with_min_max(matrix)
        elif choice == "6":
            matrix = matrices.read_matrix_from_file(DATA_MATRIX)
            value = input_int("Значение с клавиатуры: ")
            graphics.draw_matrix_colored_rows(matrix, value)
        elif choice == "7":
            matrix = matrices.read_matrix_from_file(DATA_MATRIX)
            graphics.draw_matrix_colored_columns(matrix)
        elif choice == "8":
            matrix = matrices.read_matrix_from_file(DATA_MATRIX)
            graphics.draw_sorted_matrix_gradient(matrix)
        elif choice == "0":
            return
        else:
            print("Неизвестный пункт меню.")


def main() -> None:
    while True:
        print_menu("Главное меню", [
            "Работа с файлами",
            "Векторы",
            "Операции с векторами",
            "Матрицы",
            "Сортировки матриц",
            "Строки",
            "Графика Tkinter",
        ])
        choice = input("Выбор: ")

        if choice == "1":
            file_menu()
        elif choice == "2":
            vectors_menu()
        elif choice == "3":
            vector_operations_menu()
        elif choice == "4":
            matrix_menu()
        elif choice == "5":
            sorting_menu()
        elif choice == "6":
            string_menu()
        elif choice == "7":
            graphics_menu()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неизвестный пункт меню.")


if __name__ == "__main__":
    main()
