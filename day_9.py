import ut
import itertools

preamble_size = 25
numbers = [int(line) for line in ut.read_input().splitlines()]


def is_valid(index):
    valid_pairs = (itertools.combinations(numbers[index-preamble_size:index], 2))
    valid_sums = dict.fromkeys(list(map(sum, valid_pairs)), True)
    return valid_sums.get(numbers[index], False)


def find_invalid_number():
    for index in range(preamble_size, len(numbers)):
        if not is_valid(index):
            return numbers[index]


def find_encryption_weakness():
    invalid_number = find_invalid_number()
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            contiguous_range = numbers[i:j+1]
            if sum(contiguous_range) == invalid_number:
                return min(contiguous_range) + max(contiguous_range)


def part_one():
    answer = find_invalid_number()
    ut.print_answer(answer)


def part_two():
    answer = find_encryption_weakness()
    ut.print_answer(answer)


