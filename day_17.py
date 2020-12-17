import ut
import itertools


def get_initial_active(dimensions):
    initial_active = {}
    raw_map = ut.read_input().splitlines()
    for y in range(len(raw_map)):
        for x in range(len(raw_map[0])):

            if dimensions == 3:
                initial_active[(x, y, 0)] = raw_map[y][x]
            elif dimensions == 4:
                initial_active[(x, y, 0, 0)] = raw_map[y][x]

    return initial_active


def get_delta_positions(dimensions):
    if dimensions == 3:
        delta_positions = list(itertools.product([-1, 0, 1], repeat=3))
        delta_positions.remove((0, 0, 0))

    elif dimensions == 4:
        delta_positions = list(itertools.product([-1, 0, 1], repeat=4))
        delta_positions.remove((0, 0, 0, 0))

    return delta_positions


class ConwayDimension:

    def __init__(self, dimensions):
        self.active = get_initial_active(dimensions)
        self.inactive_to_update = []
        self.delta_positions = get_delta_positions(dimensions)

    def get_neighbours(self, pos):
        return [ut.pos_add(pos, delta_pos) for delta_pos in self.delta_positions]

    # updates a single position in the grid, return the status of the updated position
    def update(self, pos):
        neighbours = self.get_neighbours(pos)
        active_neighbours = 0

        for neighbour in neighbours:
            if self.active.get(neighbour, '.') == '#':
                active_neighbours += 1
            else:
                self.inactive_to_update.append(neighbour)

        if self.active.get(pos, '.') == '#':
            if active_neighbours in [2, 3]:
                return '#'
            else:
                return '.'
        else:
            if active_neighbours == 3:
                return '#'
            else:
                return '.'

    def update_positions(self, positions_to_update, new_grid_state):
        for pos_to_update in positions_to_update:
            new_status = self.update(pos_to_update)

            # only add to active if the new status is active
            if new_status == '#':
                new_grid_state[pos_to_update] = '#'
        return new_grid_state

    # Update the 3d grid one cycle
    def cycle(self):
        active_to_update = self.active.copy()
        self.inactive_to_update = []

        # update all previously active cubes
        new_active = self.update_positions(active_to_update, {})

        # update all inactive neighbours
        inactive_to_update = dict.fromkeys(self.inactive_to_update).keys()
        new_active = self.update_positions(inactive_to_update, new_active)

        # update the active
        self.active = new_active


def part_one():
    conway_dimension = ConwayDimension(3)
    cycles = 6
    for i in range(cycles):
        conway_dimension.cycle()
    ut.print_answer(len(conway_dimension.active))


def part_two():
    conway_dimension = ConwayDimension(4)
    cycles = 6
    for i in range(cycles):
        conway_dimension.cycle()
    ut.print_answer(len(conway_dimension.active))



