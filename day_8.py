import ut


class HandheldGameConsole:

    def __init__(self, instructions):
        self.pointer = 0
        self.accumulator = 0
        self.run_instructions = {}
        self.instructions = instructions
        self.operations = {
            'nop': self.nop,
            'acc': self.acc,
            'jmp': self.jmp
        }

    def nop(self, arg):
        return

    def acc(self, arg):
        self.accumulator += arg

    def jmp(self, arg):
        self.pointer += arg - 1

    def do_instruction(self):
        self.run_instructions[self.pointer] = True
        instruction = self.instructions[self.pointer]
        operation = self.operations[instruction[0]]
        arg = int(instruction[1])
        operation(arg)
        self.pointer += 1

    def run(self):
        while 0 <= self.pointer < len(self.instructions):
            if self.run_instructions.get(self.pointer, False):
                return
            else:
                self.do_instruction()


def get_repaired_instructions():
    instructions = [line.split() for line in ut.read_input().splitlines()]
    repaired_instructions = []

    for index, instruction in enumerate(instructions):
        operation = instruction[0]
        arg = instruction[1]
        if operation == 'nop':
            repaired_instruction = instructions.copy()
            repaired_instruction[index] = ['jmp', arg]
            repaired_instructions.append(repaired_instruction)
        elif operation == 'jmp':
            repaired_instruction = instructions.copy()
            repaired_instruction[index] = ['nop', arg]
            repaired_instructions.append(repaired_instruction)

    return repaired_instructions


def part_two():
    repaired_instructions = get_repaired_instructions()
    for instructions in repaired_instructions:
        hgc = HandheldGameConsole(instructions)
        hgc.run()
        if hgc.pointer == len(instructions):
            ut.print_answer(hgc.accumulator)


def part_one():
    instructions = [line.split() for line in ut.read_input().splitlines()]
    hgc = HandheldGameConsole(instructions)
    hgc.run()
    ut.print_answer(hgc.accumulator)



