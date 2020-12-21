import ut

input_data = ut.read_input().split('\n\n')
messages = input_data[1].splitlines()


def gen_rules():
    raw_rules = input_data[0].splitlines()
    all_rules = {}
    for rule in raw_rules:
        rule = rule.split(': ')
        rule_no = rule[0]
        rule_branches = []
        for rule_branch in rule[1].split(' | '):
            rule_branches.append(rule_branch.split())
        all_rules[rule_no] = rule_branches
    return all_rules


rules = gen_rules()


def get_valid_messages(rule_no):
    valid_messages = []

    for branch in rules[rule_no]:
        valid_messages_branch = []
        for el in branch:

            if str.isnumeric(el):
                branch_messages = get_valid_messages(el)
                new_valid_messages_branch = []
                if valid_messages_branch:
                    for branch_message in branch_messages:
                        new_valid_messages_branch += [message + branch_message for message in valid_messages_branch]
                    valid_messages_branch = new_valid_messages_branch
                else:
                    valid_messages_branch = branch_messages

            elif str.isalpha(el):
                if valid_messages_branch:
                    valid_messages_branch = [message + el for message in valid_messages_branch]
                else:
                    valid_messages_branch = [el]
        valid_messages += valid_messages_branch
    return valid_messages


rule_42 = dict.fromkeys(get_valid_messages('42'), True)
rule_31 = dict.fromkeys(get_valid_messages('31'), True)


def get_8_chunks(message):
    chunks = []
    if len(message) % 8 == 0 and len(message) >= 8*3:
        for i in range(0, len(message), 8):
            chunks.append(message[i:i+8])
    return chunks


def is_valid_message(message):
    eight_chunks = get_8_chunks(message)
    eight_chunks.reverse()

    if not eight_chunks:
        return False

    for y in range(1, len(eight_chunks)):
        if len(eight_chunks) - y*2 >= 1:
            chunks = eight_chunks[0:y]
            if all([rule_31.get(chunk, False) for chunk in chunks]):
                if all([rule_42.get(rest_chunk, False) for rest_chunk in eight_chunks[y:]]):
                    return True
    return False


def part_one():
    valid_messages = dict.fromkeys(get_valid_messages('0'), 1)
    answer = sum([valid_messages.get(message, 0) for message in messages])
    ut.print_answer(answer)


def part_two():
    answer = [is_valid_message(message) for message in messages].count(True)
    ut.print_answer(answer)


part_two()

