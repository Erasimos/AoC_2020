import math
delta_positions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def read_file(path):
    file = open(path, "r")
    contents = file.read()
    return contents


def read_input():
    file = open('input.txt', "r")
    contents = file.read()
    return contents


def pos_add(pos_1, pos_2):
    new_pos = []
    for i in range(len(pos_1)):
        new_pos.append(pos_1[i] + pos_2[i])
    return tuple(new_pos)


def rotate_point_around_point(origin, point, angle):
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


def pos_mul(pos, factor):
    new_x = pos[0] * factor
    new_y = pos[1] * factor
    return new_x, new_y


def lcm(numbers):
    lcm = numbers[0]
    for i in numbers[1:]:
        lcm = lcm * i // math.gcd(lcm, i)
    return lcm


def udlr_neighbours(pos):
    return [pos_add(pos, delta_pos) for delta_pos in delta_positions]


def print_answer(answer):
    print('Answer is: ' + str(answer))
