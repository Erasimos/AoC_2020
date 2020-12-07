import ut

group_answers = ut.read_input().split("\n\n")


def count_answers(group):
    group = "".join(group.split("\n"))
    return len(dict.fromkeys(list(group)).keys())


def count_answers_v2(group):
    group_size = len(group.split("\n"))
    answers = {}
    for char in "".join(group.split("\n")):
        val = answers.get(char, 0)
        answers[char] = 1 + val

    count = 0
    for val in answers.values():
        if val == group_size:
            count += 1
    return count


def part_one():
    answer = sum([count_answers(group) for group in group_answers])
    ut.print_answer(answer)


def part_two():
    answer = sum([count_answers_v2(group) for group in group_answers])
    ut.print_answer(answer)


part_two()

