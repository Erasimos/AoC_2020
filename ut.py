

def read_file(path):
    file = open(path, "r")
    contents = file.read()
    return contents


def read_input():
    file = open('input.txt', "r")
    contents = file.read()
    return contents


def pos_add(pos_1, pos_2):
    return pos_1[0] + pos_2[0], pos_1[1] + pos_2[1]


def print_answer(answer):
    print('Answer is: ' + str(answer))
