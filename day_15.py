import ut

starting_sequence = [1, 0, 18, 10, 19, 6]
occurrences = {}
last_turn = {}
for index, number in enumerate(starting_sequence):
    occurrences[number] = 1
    last_turn[number] = index


def play(turns):
    prev_num = starting_sequence[-1]
    for turn in range(len(starting_sequence), turns):

        if occurrences[prev_num] == 1:
            next_num = 0
        else:
            next_num = turn - 1 - last_turn[prev_num]

        last_turn[prev_num] = turn - 1
        occurrences[next_num] = occurrences.get(next_num, 0) + 1
        prev_num = next_num

    return prev_num


def part_one():
    ut.print_answer(play(2020))


def part_two():
    ut.print_answer(play(30000000))

