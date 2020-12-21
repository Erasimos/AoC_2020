import ut


directions = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
seats = ut.read_input().splitlines()


def get_seat_map():
    seat_map = {}
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            seat_map[(row, col)] = seats[row][col]
    return seat_map


def print_map(grid):
    for row in range(10):
        for col in range(10):
            print(grid[(row, col)], end='')
        print()
    print()


def get_neighbours(pos):
    return [ut.pos_add(pos, direction) for direction in directions]


def in_bounds(pos):
    return 0 <= pos[0] < len(seats) and 0 <= pos[1] < len(seats[0])


def get_neighbours_v2(pos, grid: dict):
    neighbours = []
    for direction in directions:
        current_pos = ut.pos_add(pos, direction)
        while in_bounds(current_pos) and grid[current_pos] == '.':
            current_pos = ut.pos_add(current_pos, direction)
        neighbours.append(grid.get(current_pos, '.'))
    return neighbours


def get_occupied_seats(pos, grid: dict):
    neighbours = get_neighbours(pos)
    occupied_seats = 0
    for neighbour in neighbours:
        if grid.get(neighbour, '.') == '#':
            occupied_seats += 1
    return occupied_seats


def get_occupied_seats_v2(pos, grid: dict):
    neighbours = get_neighbours_v2(pos, grid)
    return neighbours.count('#')


def simulate(grid: dict):
    updated_grid = grid.copy()
    changes = False
    for pos in grid.keys():
        if grid[pos] == '.':
            continue
        occupied_seats = get_occupied_seats(pos, grid)
        if grid[pos] == 'L' and occupied_seats == 0:
            updated_grid[pos] = '#'
            changes = True
        elif grid[pos] == '#' and occupied_seats >= 4:
            updated_grid[pos] = 'L'
            changes = True
    return updated_grid, changes


def simulate_v2(grid: dict):
    updated_grid = grid.copy()
    changes = False
    for pos in grid.keys():
        if grid[pos] == '.':
            continue
        occupied_seats = get_occupied_seats_v2(pos, grid)
        if grid[pos] == 'L' and occupied_seats == 0:
            updated_grid[pos] = '#'
            changes = True
        elif grid[pos] == '#' and occupied_seats >= 5:
            updated_grid[pos] = 'L'
            changes = True
    return updated_grid, changes


def count_occupied_seats(grid: dict):
    count = 0
    for pos in grid.keys():
        if grid[pos] == '#':
            count += 1
    return count


def part_one():
    seat_map = get_seat_map()
    changes = True
    while changes:
        seat_map, changes = simulate(seat_map)
    ut.print_answer(count_occupied_seats(seat_map))


def part_two():
    seat_map = get_seat_map()
    changes = True
    while changes:
        seat_map, changes = simulate_v2(seat_map)
    ut.print_answer(count_occupied_seats(seat_map))




