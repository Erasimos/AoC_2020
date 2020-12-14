import ut


def get_instructions():
    instructions = [line.split(' = ') for line in ut.read_input().splitlines()]
    for index, instruction in enumerate(instructions):
        operation = instruction[0]
        if operation[0:3] == 'mem':
            address = operation.split('mem[')[1].split(']')[0]
            instructions[index] = ['mem', (int(address), int(instruction[1]))]
    return instructions


class Program:

    def __init__(self):
        self.memory = {}
        self.mask = ''
        self.operations = {'mask': self.set_mask, 'mem': self.mem}

    def initialize(self, instructions):
        for instruction in instructions:
            operation = instruction[0]
            arg = instruction[1]
            self.operations[operation](arg)

    def set_mask(self, new_mask):
        self.mask = new_mask

    def apply_mask(self, val):
        masked_value = list('{:036b}'.format(val))
        for index in range(len(masked_value)):
            if not self.mask[index] == 'X':
                masked_value[index] = self.mask[index]
        return masked_value

    def mem(self, arg):
        address = arg[0]
        val = arg[1]
        masked_value = self.apply_mask(val)
        self.memory[address] = masked_value

    def sum_memory(self):
        return sum([int(''.join(val), 2) for val in self.memory.values()])


class ProgramV2:

    def __init__(self):
        self.memory = {}
        self.mask = ''
        self.operations = {'mask': self.set_mask, 'mem': self.mem}

    def initialize(self, instructions):
        for instruction in instructions:
            operation = instruction[0]
            arg = instruction[1]
            self.operations[operation](arg)

    def set_mask(self, new_mask):
        self.mask = new_mask

    def apply_mask(self, val):
        masked_value = list('{:036b}'.format(val))
        addresses_to_write = [masked_value]
        for index, bit in enumerate(self.mask):
            if bit == 'X':
                expanded_addresses_to_write = []
                for i in range(len(addresses_to_write)):
                    address_1 = addresses_to_write[i].copy()
                    address_1[index] = '1'

                    address_2 = addresses_to_write[i].copy()
                    address_2[index] = '0'

                    expanded_addresses_to_write.append(address_1)
                    expanded_addresses_to_write.append(address_2)

                addresses_to_write = expanded_addresses_to_write

            elif bit == '1':
                for i in range(len(addresses_to_write)):
                    addresses_to_write[i][index] = '1'

        return addresses_to_write

    def mem(self, arg):
        address = arg[0]
        val = arg[1]
        addresses_to_write = self.apply_mask(address)
        for address_to_write in addresses_to_write:
            self.memory[int(''.join(address_to_write), 2)] = int(val)

    def sum_memory(self):
        return sum([val for val in self.memory.values()])


def part_one():
    program = Program()
    instructions = get_instructions()
    program.initialize(instructions)
    ut.print_answer(program.sum_memory())


def part_two():
    program = ProgramV2()
    instructions = get_instructions()
    program.initialize(instructions)
    ut.print_answer(program.sum_memory())

