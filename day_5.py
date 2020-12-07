import ut

boarding_passes = ut.read_input().splitlines()


def get_row_col(seat, high_bound):
    low = 0
    high = high_bound

    for char in seat:
        half = ((high - low) / 2)
        if char in ["B", "R"]:
            low += half
        elif char in ["F", "L"]:
            high -= half
    return int(high) - 1


def get_seat_id(boarding_pass):
    row, col = get_seat(boarding_pass)
    seat_id = row * 8 + col
    return seat_id


def get_seat(boarding_pass):
    row = get_row_col(boarding_pass[0:7], 128)
    col = get_row_col(boarding_pass[7:], 8)
    return row, col


def part_one():
    max_id = max([get_seat_id(b_pass) for b_pass in boarding_passes])
    ut.print_answer(max_id)


def part_two():
    sorted_seats = sorted(boarding_passes, key=get_seat_id)
    for i in range(1, len(sorted_seats) - 1):
        prev_seat_id = get_seat_id(sorted_seats[i-1])
        next_seat_id = get_seat_id(sorted_seats[i])
        if next_seat_id - prev_seat_id > 1:
            print(get_seat(sorted_seats[i-1]))
            print(get_seat(sorted_seats[i]))

