import ut

expense_report = [int(val) for val in ut.read_file('input.txt').splitlines()]


def part_one():
    for i in range(len(expense_report)):
        for j in range(i + 1, len(expense_report)):
            val_1 = expense_report[i]
            val_2 = expense_report[j]
            if val_1 + val_2 == 2020:
                ut.print_answer(val_1 * val_2)


def part_two():
    for i in range(len(expense_report)):
        for j in range(i + 1, len(expense_report)):
            for k in range(j + 1, len(expense_report)):
                val_1 = expense_report[i]
                val_2 = expense_report[j]
                val_3 = expense_report[k]
                if val_1 + val_2 + val_3 == 2020:
                    ut.print_answer(val_1 * val_2 * val_3)
