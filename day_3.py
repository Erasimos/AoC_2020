import ut

forest = ut.read_input().splitlines()


def is_tree(pos):
    col = pos[0] % len(forest[0])
    row = pos[1]
    return forest[row][col] == '#'


def ride(slope):
    pos = (0, 0)
    trees = 0

    while pos[1] < len(forest) - 1:
        pos = ut.pos_add(pos, slope)
        if is_tree(pos):
            trees += 1

    return trees


def part_one():
    slope = (3, 1)
    trees = ride(slope)
    ut.print_answer(trees)


def part_two():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    answer = 1
    for slope in slopes:
        answer *= ride(slope)
    ut.print_answer(answer)


part_two()

