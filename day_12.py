import ut

boat_instructions = ut.read_input().splitlines()


class Boat:

    def __init__(self):
        self.start_pos = (0, 0)
        self.current_pos = (0, 0)
        self.facing = ('E', 1)
        self.directions = ['N', 'E', 'S', 'W']
        self.delta_directions = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
        self.navigation = {
            'N': self.N,
            'E': self.E,
            'S': self.S,
            'W': self.W,
            'R': self.R,
            'L': self.L,
            'F': self.F
            }

    def N(self, units):
        delta_pos = ut.pos_mul(self.delta_directions['N'], units)
        self.current_pos = ut.pos_add(self.current_pos, delta_pos)

    def E(self, units):
        delta_pos = ut.pos_mul(self.delta_directions['E'], units)
        self.current_pos = ut.pos_add(self.current_pos, delta_pos)

    def S(self, units):
        delta_pos = ut.pos_mul(self.delta_directions['S'], units)
        self.current_pos = ut.pos_add(self.current_pos, delta_pos)

    def W(self, units):
        delta_pos = ut.pos_mul(self.delta_directions['W'], units)
        self.current_pos = ut.pos_add(self.current_pos, delta_pos)

    def R(self, degrees):
        steps = int(degrees / 90)
        current_step = self.facing[1]
        new_step = (current_step + steps) % 4
        new_facing = self.directions[new_step]
        self.facing = (new_facing, new_step)

    def L(self, degrees):
        steps = int(degrees / 90)
        current_step = self.facing[1]
        new_step = (current_step - steps) % 4
        new_facing = self.directions[new_step]
        self.facing = (new_facing, new_step)

    def F(self, units):
        delta_pos = ut.pos_mul(self.delta_directions[self.facing[0]], units)
        self.current_pos = ut.pos_add(self.current_pos, delta_pos)

    def navigate(self, action, arg):
        self.navigation[action](arg)

    def follow_instructions(self, instructions):
        for instruction in instructions:
            action = instruction[0]
            arg = int(instruction[1:])
            self.navigate(action, arg)

    def get_manhattan_distance_traveled(self):
        x_diff = self.start_pos[0] - self.current_pos[0]
        y_diff = self.start_pos[1] - self.current_pos[1]
        return abs(x_diff) + abs(y_diff)


class WayPointBoat:

    def __init__(self):
        self.start_pos = (0, 0)
        self.current_pos = (0, 0)
        self.way_point_pos = (10, 1)
        self.facing = ('E', 1)
        self.directions = ['N', 'E', 'S', 'W']
        self.delta_directions = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
        self.navigation = {
            'N': self.N,
            'E': self.E,
            'S': self.S,
            'W': self.W,
            'R': self.R,
            'L': self.L,
            'F': self.F
            }

    def N(self, units):
        delta_pos = ut.pos_mul(self.delta_directions['N'], units)
        self.way_point_pos = ut.pos_add(self.way_point_pos, delta_pos)

    def E(self, units):
        delta_pos = ut.pos_mul(self.delta_directions['E'], units)
        self.way_point_pos = ut.pos_add(self.way_point_pos, delta_pos)

    def S(self, units):
        delta_pos = ut.pos_mul(self.delta_directions['S'], units)
        self.way_point_pos = ut.pos_add(self.way_point_pos, delta_pos)

    def W(self, units):
        delta_pos = ut.pos_mul(self.delta_directions['W'], units)
        self.way_point_pos = ut.pos_add(self.way_point_pos, delta_pos)

    def R(self, degrees):
        steps = int(degrees / 90)
        for step in range(steps):
            old_x = self.way_point_pos[0]
            old_y = self.way_point_pos[1]
            new_x = old_y
            new_y = -old_x
            self.way_point_pos = (new_x, new_y)

    def L(self, degrees):
        steps = int(degrees / 90)
        for step in range(steps):
            old_x = self.way_point_pos[0]
            old_y = self.way_point_pos[1]
            new_x = -old_y
            new_y = old_x
            self.way_point_pos = (new_x, new_y)

    def F(self, units):
        x_delta = self.way_point_pos[0] * units
        y_delta = self.way_point_pos[1] * units
        delta_pos = (x_delta, y_delta)
        self.current_pos = ut.pos_add(self.current_pos, delta_pos)

    def navigate(self, action, arg):
        self.navigation[action](arg)

    def follow_instructions(self, instructions):
        for instruction in instructions:
            print(instruction)
            action = instruction[0]
            arg = int(instruction[1:])
            self.navigate(action, arg)
            print(self.current_pos)
            print(self.way_point_pos)
            print()

    def get_manhattan_distance_traveled(self):
        x_diff = self.start_pos[0] - self.current_pos[0]
        y_diff = self.start_pos[1] - self.current_pos[1]
        return abs(x_diff) + abs(y_diff)


def part_one():
    boat = Boat()
    boat.follow_instructions(boat_instructions)
    ut.print_answer(boat.get_manhattan_distance_traveled())


def part_two():
    boat = WayPointBoat()
    boat.follow_instructions(boat_instructions)
    ut.print_answer(boat.get_manhattan_distance_traveled())

