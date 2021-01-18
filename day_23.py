import ut
starting_cups = [int(el) for el in ut.read_input()]


def move_v2(cups: dict, current_cup):

    next_val = cups[current_cup]
    next_next_val = cups[next_val]
    next_next_next_val = cups[next_next_val]
    target = current_cup - 1
    while True:
        target = len(cups) if target == 0 else target
        if target in [next_val, next_next_val, next_next_next_val]:
            target = target - 1
        else:
            break
    next_current = cups[next_next_next_val]
    cups[next_next_next_val] = cups[target]
    cups[target] = next_val
    cups[current_cup] = next_current

    return cups, next_current


def move(current_cup, cups: list):
    cut = [cups[(i + current_cup) % len(cups)] for i in range(1, 4)]
    keep = cups[0:current_cup + 1] + cups[current_cup + 4:] if (current_cup + 4) % len(cups) > current_cup \
        else cups[(current_cup + 4 % len(cups)):current_cup + 1]
    destination_index = "None"
    target = (cups[current_cup] - 1)
    while destination_index == "None":
        target = len(cups) if target == 0 else target
        if target not in cut:
            destination_index = keep.index(target)
        else:
            target = target - 1

    #new_cups = keep[0:destination_index + 1] + cut + keep[destination_index + 1:]
    cups = keep[current_cup:destination_index + 1] + cut + keep[destination_index + 1:] + keep[0:current_cup]
    #new_current_cup = (new_cups.index(cups[current_cup]) + 1) % len(cups)
    return 1, cups


def part_one():
    cups = {}
    for index, cup in enumerate(starting_cups):
        cups[cup] = starting_cups[(index + 1) % len(starting_cups)]

    current_cup = 3
    print(cups)
    for i in range(10):
        cups, current_cup = move_v2(cups, current_cup)
        print(cups)

    print("-- final --")
    print(cups)


def part_two():

    max_num = max(starting_cups)
    for i in range(1000000 - len(starting_cups)):
        starting_cups.append(i + max_num + 1)

    cups = {}
    for index, cup in enumerate(starting_cups):
        cups[cup] = starting_cups[(index + 1) % len(starting_cups)]

    current_cup = 3
    for i in range(10000000):
        cups, current_cup = move_v2(cups, current_cup)
    print(cups[1])
    print(cups[cups[1]])
    ut.print_answer(cups[1] * cups[cups[1]])


part_two()