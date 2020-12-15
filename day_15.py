import ut

starting_sequence = [1, 0, 18, 10, 19, 6]
occurrences = {}
last_turn = {}
for index, number in enumerate(starting_sequence):
    occurrences[number] = 1
    last_turn[number] = index


def play(turns):
    spoken_numbers = starting_sequence.copy()
    for turn in range(len(starting_sequence), turns):

        prev_num = spoken_numbers[turn - 1]
        if occurrences[prev_num] == 1:
            next_num = 0
        else:
            next_num = turn - 1 - last_turn[prev_num]

        last_turn[prev_num] = turn - 1
        spoken_numbers.append(next_num)
        occurrences[next_num] = occurrences.get(next_num, 0) + 1

    return spoken_numbers[-1]


def part_one():
    ut.print_answer(play(30000000))


part_one()
