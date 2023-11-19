import random
from queue import Queue


def generate_random_field(rows, cols, land_percentage=0.3):
    field = [[0 if random.random() > land_percentage else 1 for _ in range(cols)] for _ in range(rows)]
    return field


def print_field(field):
    for row in field:
        for cell in row:
            print('X' if cell == 1 else ' ', end=' ')
        print()


def is_valid_move(x, y, rows, cols, visited, field):
    return 0 <= x < rows and 0 <= y < cols and (x, y) not in visited and field[x][y] == 0


def get_neighbors(x, y):
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


def find_shortest_path(field, start, end):
    rows, cols = len(field), len(field[0])
    queue = Queue()
    queue.put((start, [start]))
    visited = {start}

    while not queue.empty():
        (x, y), path = queue.get()
        if (x, y) == end:
            return path

        for nx, ny in get_neighbors(x, y):
            if is_valid_move(nx, ny, rows, cols, visited, field):
                new_path = path + [(nx, ny)]
                if (nx, ny) == end:
                    return new_path
                queue.put(((nx, ny), new_path))
                visited.add((nx, ny))

    return None


def main():
    try:
        rows = int(input("Введите количество строк поля (M): "))
        cols = int(input("Введите количество столбцов поля (N): "))
        start = tuple(int(input(f"Введите координату {coord} начальной точки A: ")) for coord in ('X', 'Y'))
        end = tuple(int(input(f"Введите координату {coord} конечной точки B: ")) for coord in ('X', 'Y'))
    except ValueError:
        print("Пожалуйста, введите целые числа.")
        return

    field = generate_random_field(rows, cols)
    print("\nСгенерированное поле:")
    print_field(field)

    path = find_shortest_path(field, start, end)

    print(f"\nКратчайший путь от {start} до {end}: {path}" if path else "\nПуть не найден.")

if __name__ == '__main__':
    main()
