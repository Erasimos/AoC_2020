import ut


adapters = [int(line) for line in ut.read_input().splitlines()]
adapters.append(max(adapters) + 3)
adapters.append(0)
adapters.sort()


def part_one():
    jolt_diff = []
    jolt = 0

    for adapter in adapters:
        jolt_diff.append(adapter - jolt)
        jolt = adapter
    one_diff_count = jolt_diff.count(1)
    three_diff_count = jolt_diff.count(3)

    ut.print_answer(one_diff_count * three_diff_count)


def count_arrangements():
    paths = dict.fromkeys(adapters, 0)
    paths[0] = 1

    for index, adapter in enumerate(adapters[0:-1]):
        i = index + 1
        while i < len(adapters) and adapters[i] - adapter <= 3:
            paths[adapters[i]] += paths[adapter]
            i += 1
    return paths[adapters[-1]]


def part_two():
    answer = count_arrangements()
    ut.print_answer(answer)


