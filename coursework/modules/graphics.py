"""Модуль графических задач на Tkinter."""

import random
import tkinter as tk

from .matrix_sorting import sort_matrix_elements


def _create_window(title: str, width: int = 700, height: int = 500) -> tuple[tk.Tk, tk.Canvas]:
    root = tk.Tk()
    root.title(title)
    canvas = tk.Canvas(root, width=width, height=height, bg="white")
    canvas.pack(fill="both", expand=True)
    return root, canvas


def draw_square() -> None:
    root, canvas = _create_window("Квадрат")
    canvas.create_rectangle(200, 120, 500, 420, outline="blue", width=3)
    root.mainloop()


def triangle_in_circle(radius: int) -> None:
    root, canvas = _create_window("Треугольник в круге")
    cx, cy = 350, 250
    canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, outline="black", width=2)

    p1 = (cx, cy - radius)
    p2 = (cx - int(radius * 0.866), cy + int(radius * 0.5))
    p3 = (cx + int(radius * 0.866), cy + int(radius * 0.5))

    canvas.create_polygon([p1, p2, p3], outline="green", fill="", width=2)
    root.mainloop()


def overlay_small_circle_on_triangle(radius: int) -> None:
    root, canvas = _create_window("Наложение круга")
    cx, cy = 350, 250
    canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius, outline="black", width=2)

    points = [
        (cx, cy - radius),
        (cx - int(radius * 0.866), cy + int(radius * 0.5)),
        (cx + int(radius * 0.866), cy + int(radius * 0.5)),
    ]
    canvas.create_polygon(points, outline="green", fill="", width=2)

    center = random.choice(points)
    r_small = radius // 4
    canvas.create_oval(
        center[0] - r_small,
        center[1] - r_small,
        center[0] + r_small,
        center[1] + r_small,
        outline="red",
        width=2,
    )
    root.mainloop()


def draw_histogram(vector: list[int]) -> None:
    root, canvas = _create_window("Гистограмма")
    if not vector:
        root.mainloop()
        return

    max_value = max(vector)
    bar_width = 500 / len(vector)

    for i, value in enumerate(vector):
        height = 300 * (value / max_value if max_value != 0 else 0)
        x1 = 80 + i * bar_width
        y1 = 420 - height
        x2 = x1 + bar_width - 5
        y2 = 420
        canvas.create_rectangle(x1, y1, x2, y2, fill="skyblue", outline="black")
        canvas.create_text((x1 + x2) / 2, y1 - 10, text=str(value))

    root.mainloop()


def draw_matrix_with_min_max(matrix: list[list[int]]) -> None:
    root, canvas = _create_window("Матрица min/max")
    values = [item for row in matrix for item in row]
    min_val, max_val = min(values), max(values)
    _draw_matrix_cells(canvas, matrix, lambda v, _i, _j: "lightgreen" if v == min_val else "salmon" if v == max_val else "white")
    root.mainloop()


def draw_matrix_colored_rows(matrix: list[list[int]], keyboard_value: int) -> None:
    root, canvas = _create_window("Окраска строк")
    colors = ["#f0f8ff", "#e6e6fa", "#fffacd", "#ffe4e1", "#e0ffff", "#f5f5dc"]

    def picker(_v: int, i: int, _j: int) -> str:
        return colors[(i + keyboard_value) % len(colors)]

    _draw_matrix_cells(canvas, matrix, picker)
    root.mainloop()


def draw_matrix_colored_columns(matrix: list[list[int]]) -> None:
    root, canvas = _create_window("Окраска столбцов")
    colors = ["#ffd1dc", "#c1f0c1", "#cde7ff", "#fff4b3", "#f2d0ff", "#d7f9f1"]

    def picker(row_value: int, _i: int, j: int) -> str:
        index = (len(colors) - 1 - j - row_value) % len(colors)
        return colors[index]

    _draw_matrix_cells(canvas, matrix, picker)
    root.mainloop()


def draw_sorted_matrix_gradient(matrix: list[list[int]]) -> None:
    sorted_matrix = sort_matrix_elements(matrix, "selection")
    root, canvas = _create_window("Отсортированная матрица с градиентом")

    diag = [sorted_matrix[i][i] for i in range(min(len(sorted_matrix), len(sorted_matrix[0])))]
    max_diag = max(diag) if diag else 1

    def picker(_v: int, i: int, _j: int) -> str:
        d = diag[i] if i < len(diag) else 0
        intensity = int(255 - (d / max_diag) * 180) if max_diag != 0 else 255
        intensity = max(60, min(255, intensity))
        return f"#{intensity:02x}{intensity:02x}ff"

    _draw_matrix_cells(canvas, sorted_matrix, picker)
    root.mainloop()


def _draw_matrix_cells(canvas: tk.Canvas, matrix: list[list[int]], color_picker) -> None:
    cell_w = 60
    cell_h = 40
    start_x = 50
    start_y = 50

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            x1 = start_x + j * cell_w
            y1 = start_y + i * cell_h
            x2 = x1 + cell_w
            y2 = y1 + cell_h
            color = color_picker(value, i, j)
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
            canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=str(value))
