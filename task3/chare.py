import random
from queue import Queue


def bfs(field, start, end):
    m, n = len(field), len(field[0])
    queue = Queue()
    queue.put((start, [start]))
    visited = {start}

    while not queue.empty():
        (x, y), path = queue.get()
        if (x, y) == end:
            return path

        for nx, ny in get_neighbors(x, y):
            if is_valid_move(nx, ny, m, n, visited):
                visited.add((nx, ny))
                if field[nx][ny] == 0 or (nx, ny) == end:
                    queue.put(((nx, ny), path + [(nx, ny)]))

    return None


def generate_field(m, n):
    field = [[0 if random.random() > 0.3 else 1 for _ in range(n)] for _ in range(m)]
    return field


def print_field(field):
    for row in field:
        print(' '.join('X' if cell == 1 else ' ' for cell in row))


def is_valid_move(x, y, m, n, visited):
    return 0 <= x < m and 0 <= y < n and (x, y) not in visited


def get_neighbors(x, y):
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


def main():
    try:
        m = int(input("Введите количество строк поля (M): "))
        n = int(input("Введите количество столбцов поля (N): "))
        start = tuple(int(input(f"Введите координату {coord} начальной точки A: ")) for coord in ('X', 'Y'))
        end = tuple(int(input(f"Введите координату {coord} конечной точки B: ")) for coord in ('X', 'Y'))
    except ValueError:
        print("Пожалуйста, введите целые числа.")
        return

    field = generate_field(m, n)
    print("\nСгенерированное поле:")
    print_field(field)

    path = bfs(field, start, end)

    print(f"\nКратчайший путь от {start} до {end}: {path}" if path else "\nПуть не найден.")


if __name__ == '__main__':
    main()
