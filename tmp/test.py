import curses
import random

# Размер сетки
GRID_SIZE = 4

# Неоновые цвета
COLORS = {
    0: curses.COLOR_BLACK,
    2: curses.COLOR_GREEN,
    4: curses.COLOR_YELLOW,
    8: curses.COLOR_CYAN,
    16: curses.COLOR_MAGENTA,
    32: curses.COLOR_RED,
    64: curses.COLOR_BLUE
}

# Функция создания окна с текстом
def print_box(window, row, col, text):
    window.addstr(row, col, text)
    window.refresh()

# Функция рисования сетки
def draw_grid(window, grid):
    window.clear()
    box_width = 9
    box_height = 5

    # Рисуем вертикальные линии
    for y in range(0, GRID_SIZE*box_height, box_height):
        for x in range(0, GRID_SIZE*box_width+1):
            window.addstr(y, x, '|')

    # Рисуем горизонтальные линии
    for x in range(0, GRID_SIZE*box_width, box_width):
        for y in range(0, GRID_SIZE*box_height+1):
            window.addstr(y, x, '-')

    # Рисуем значения в клетках
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            value = grid[i][j]
            color = COLORS.get(value, curses.COLOR_WHITE)
            window.attron(curses.color_pair(color))
            window.addstr(i*box_height+2, j*box_width+2, str(value).center(5))
            window.attroff(curses.color_pair(color))

    window.refresh()

# Функция инициализации пустой сетки
def initialize_grid():
    return [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

# Функция добавления новой плитки на сетку
def add_new_tile(grid):
    empty_cells = []
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 0:
                empty_cells.append((i, j))
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = random.choice([2, 4])
    return grid

# Функция поворота сетки на 90 градусов по часовой стрелке
def rotate_grid(grid):
    return [list(row) for row in zip(*grid[::-1])]

# Функция сдвига значений в сетке влево
def slide_left(grid):
    new_grid = []
    for row in grid:
        new_row = []
        for value in row:
            if value != 0:
                new_row.append(value)
        new_row += [0] * (GRID_SIZE - len(new_row))
        new_grid.append(new_row)
    return new_grid

# Функция объединения соседних значений в сетке
def merge_values(grid):
    for row in grid:
        for i in range(GRID_SIZE - 1):
            if row[i] == row[i+1] and row[i] != 0:
                row[i] *= 2
                row[i+1] = 0
    return grid

# Функция проверки возможности сдвига в заданном направлении
def can_slide(grid, direction):
    rotated_grid = grid
    if direction == 'up':
        rotated_grid = rotate_grid(rotated_grid)
    elif direction == 'right':
        rotated_grid = rotate_grid(rotate_grid(rotated_grid))
    elif direction == 'down':
        rotated_grid = rotate_grid(rotate_grid(rotate_grid(rotated_grid)))
    for row in rotated_grid:
        for i in range(GRID_SIZE - 1):
            if row[i] == 0 and row[i+1] != 0:
                return True
            if row[i] != 0 and row[i] == row[i+1]:
                return True
    return False

# Функция сдвига значений в сетке в указанном направлении
def slide(grid, direction):
    new_grid = grid
    if direction == 'up':
        new_grid = rotate_grid(grid)
    elif direction == 'right':
        new_grid = rotate_grid(rotate_grid(grid))
    elif direction == 'down':
        new_grid = rotate_grid(rotate_grid(rotate_grid(grid)))
    new_grid = slide_left(new_grid)
    new_grid = merge_values(new_grid)
    new_grid = slide_left(new_grid)
    if direction == 'up':
        new_grid = rotate_grid(new_grid)
    elif direction == 'right':
        new_grid = rotate_grid(rotate_grid(new_grid))
    elif direction == 'down':
        new_grid = rotate_grid(rotate_grid(rotate_grid(new_grid)))
    return new_grid

# Функция проверки окончания игры
def is_game_over(grid):
    directions = ['up', 'right', 'down', 'left']
    for direction in directions:
        if can_slide(grid, direction):
            return False
    return True

# Инициализация curses и создание окна
stdscr = curses.initscr()
curses.start_color()
curses.use_default_colors()
for i in range(0, curses.COLORS):
    curses.init_pair(i, i, -1)
stdscr.keypad(True)
curses.noecho()
curses.curs_set(0)
stdscr.nodelay(True)

# Инициализация сетки и добавление первых двух плиток
grid = initialize_grid()
grid = add_new_tile(grid)
grid = add_new_tile(grid)

# Основной цикл игры
while True:
    stdscr.clear()
    draw_grid(stdscr, grid)
    if is_game_over(grid):
        print_box(stdscr, 10, 10, "Game Over")
        break
    key = stdscr.getch()
    if key == ord('q'):
        break
    elif key == curses.KEY_UP:
        if can_slide(grid, 'up'):
            grid = slide(grid, 'up')
            grid = add_new_tile(grid)
    elif key == curses.KEY_RIGHT:
        if can_slide(grid, 'right'):
            grid = slide(grid, 'right')
            grid = add_new_tile(grid)
    elif key == curses.KEY_DOWN:
        if can_slide(grid, 'down'):
            grid = slide(grid, 'down')
            grid = add_new_tile(grid)
    elif key == curses.KEY_LEFT:
        if can_slide(grid, 'left'):
            grid = slide(grid, 'left')
            grid = add_new_tile(grid)

# Завершение curses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
