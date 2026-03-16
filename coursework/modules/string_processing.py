"""Модуль для обработки строковых задач."""


def format_text(text: str, width: int = 50) -> tuple[str, str, str]:
    """Возвращает текст по левому, центру и правому краю."""
    return text.ljust(width), text.center(width), text.rjust(width)


def draw_ascii_table(rows: int, cols: int, cell_width: int = 5) -> str:
    """Строит таблицу псевдографикой."""
    horizontal = "+" + ("-" * cell_width + "+") * cols
    middle = "|" + (" " * cell_width + "|") * cols

    lines = []
    for _ in range(rows):
        lines.append(horizontal)
        lines.append(middle)
    lines.append(horizontal)
    return "\n".join(lines)


def remove_chars_from_file_line(filename: str, chars: str) -> str:
    """Читает первую строку файла и удаляет из неё заданные символы."""
    with open(filename, "r", encoding="utf-8") as file:
        line = file.readline().rstrip("\n")

    result = "".join(ch for ch in line if ch not in chars)
    return result


def search_partial_in_file(filename: str, query: str) -> int:
    """Ищет подстроку в файле и возвращает номер последней найденной строки."""
    last_line = -1
    with open(filename, "r", encoding="utf-8") as file:
        for index, line in enumerate(file, start=1):
            if query.lower() in line.lower():
                last_line = index
    return last_line


def odd_length_words_from_file(filename: str) -> list[str]:
    """Возвращает слова нечётной длины из всех строк файла."""
    words = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            for word in line.split():
                cleaned = word.strip(".,!?;:\"'()[]{}")
                if cleaned and len(cleaned) % 2 == 1:
                    words.append(cleaned)
    return words
