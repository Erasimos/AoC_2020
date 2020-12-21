import ut
import math


buses = [(13, 0), (41, 3), (569, 13), (29, 15), (19, 32), (23, 36), (937, 44), (37, 50), (17, 61)]
earliest_departure = 1007125


def get_buses():
    raw_table = ut.read_input().split(',')
    bus_table = []
    for index, bus in enumerate(raw_table):
        if not bus == 'x':
            bus_table.append((bus, index))
    return bus_table


def waiting_time(bus):
    return math.ceil(earliest_departure / bus) * bus - earliest_departure


def part_one():
    bus_id = 0
    min_wait = math.inf

    for bus in buses:
        bus_cycle = bus[0]
        wait_time = waiting_time(bus_cycle)
        if wait_time < min_wait:
            min_wait = wait_time
            bus_id = bus[0]

    ut.print_answer(bus_id * min_wait)


def is_aligned(bus, offset, time):
    return (time + offset) % bus == 0


def part_two():
    t_start = 0
    t_offset = 1

    for i in range(len(buses)):
        bus_group = buses[0:i+1]
        t = t_start
        while True:
            if all([is_aligned(bus[0], bus[1], t) for bus in bus_group]):
                ut.print_answer(t)
                t_start = t
                t_offset = ut.lcm([bus[0] for bus in bus_group])
                break
            else:
                t += t_offset

part_two()