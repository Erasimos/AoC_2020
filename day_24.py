import ut

delta_positions = {"e": (1, 0),
                   "w": (-1, 0),
                   "sw": (-0.5, -1),
                   "nw": (-0.5, 1),
                   "se": (0.5, -1),
                   "ne": (0.5, 1)}


class HexGrid:

    def __init__(self):
        self.tiles = {}
        self.dead_to_update = []
        self.new_tiles = {}

    def init_tiles(self, instructions):
        for instruction in instructions:
            pos = get_pos(instruction)
            self.flip(pos)

    def flip(self, pos):
        tile = self.tiles.get(pos, "white")
        if tile == "white":
            self.tiles[pos] = "black"
        else:
            self.tiles.pop(pos)

    def update_pos(self, pos):
        neighbour_positions = [ut.pos_add(pos, delta_pos) for delta_pos in delta_positions.values()]
        blacks = 0
        for neighbour_pos in neighbour_positions:
            if self.tiles.get(neighbour_pos, "white") == "black":
                blacks += 1
            else:
                self.dead_to_update.append(neighbour_pos)

        if self.tiles.get(pos, "white") == "white":
            if blacks == 2:
                self.new_tiles[pos] = "black"
        elif self.tiles.get(pos, "white") == "black":
            if not (blacks == 0 or blacks > 2):
                self.new_tiles[pos] = "black"

    def update(self):
        self.dead_to_update = []
        self.new_tiles = {}
        for pos in self.tiles.keys():
            self.update_pos(pos)

        for pos in dict.fromkeys(self.dead_to_update).copy():
            self.update_pos(pos)
        self.tiles = self.new_tiles.copy()

    def count_black(self):
        return len(self.tiles)


def get_pos(instruction):
    pos = (0, 0)
    for direction in instruction:
        pos = ut.pos_add(pos, delta_positions[direction])
    return pos


def get_instructions():
    raw_instructions = ut.read_input().splitlines()
    instructions = []
    for raw_instruction in raw_instructions:
        index = 0
        instruction = []
        while index < len(raw_instruction):
            char = raw_instruction[index]
            if index == len(raw_instruction) - 1:
                instruction.append(char)
            else:
                next_char = raw_instruction[index + 1]
                if char in ["e", "w"]:
                    instruction.append(char)
                else:
                    instruction.append(char + next_char)
                    index += 1
            index += 1
        instructions.append(instruction)
    return instructions


def part_one():
    hex_grid = HexGrid()
    hex_grid.init_tiles(get_instructions())
    ut.print_answer(hex_grid.count_black())


part_one()


def part_two():
    hex_grid = HexGrid()
    hex_grid.init_tiles(get_instructions())

    for i in range(100):
        hex_grid.update()
        print("day " + str(i+1) + " : " + str(hex_grid.count_black()))

part_two()

