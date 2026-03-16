"""Модуль для простых операций с файлами."""


def read_keyboard_and_print() -> None:
    """Считывает строку с клавиатуры и красиво выводит."""
    text = input("Введите строку: ")
    print(f"Вы ввели: '{text}'")


def read_keyboard_and_write_to_file(filename: str) -> None:
    """Считывает строку и записывает её в конец файла."""
    text = input("Введите строку для записи в файл: ")
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text + "\n")
    print(f"Строка записана в файл: {filename}")


def read_file_and_print(filename: str) -> None:
    """Читает файл и выводит его содержимое."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        print("Содержимое файла:")
        print(content if content else "<файл пуст>")
    except FileNotFoundError:
        print("Файл не найден.")


def write_to_file_start(filename: str) -> None:
    """Считывает строку и добавляет её в начало файла."""
    text = input("Введите строку для вставки в начало файла: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            old_data = file.read()
    except FileNotFoundError:
        old_data = ""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text + "\n" + old_data)

    print("Строка добавлена в начало файла.")
