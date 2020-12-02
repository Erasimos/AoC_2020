import ut


class PasswordPolicy:

    def __init__(self, password, policy_char, policy_range):
        self.password = password
        self.policy_char = policy_char
        self.policy_range = policy_range

    def is_valid_password(self):
        char_count = sum([1 if char == self.policy_char else 0 for char in self.password])
        return self.policy_range[0] <= char_count <= self.policy_range[1]

    def is_valid_password_v2(self):
        char_1 = self.password[self.policy_range[0] - 1]
        char_2 = self.password[self.policy_range[1] - 1]
        return not char_1 == char_2 and self.policy_char in [char_1, char_2]


def get_password_data():
    raw_password_data = [line.split(': ') for line in ut.read_file('input.txt').splitlines()]
    password_data = []
    for password in raw_password_data:
        new_password = password[1]
        policy_char = password[0].split()[1]
        policy_range = [int(val) for val in password[0].split()[0].split('-')]
        password_data.append(PasswordPolicy(new_password, policy_char, policy_range))
    return password_data


def part_one():
    password_data = get_password_data()
    count = 0
    for policy in password_data:
        if policy.is_valid_password():
            count += 1
    ut.print_answer(count)


def part_two():
    password_data = get_password_data()
    count = 0
    for policy in password_data:
        if policy.is_valid_password_v2():
            count += 1
    ut.print_answer(count)


part_two()