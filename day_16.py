import ut


class TrainRule:

    def __init__(self, name, ranges):
        self.name = name
        self.ranges = self.init_ranges(ranges)

    @staticmethod
    def init_ranges(ranges):
        rule_ranges = []
        for rule_range in ranges:
            lower_bound = int(rule_range.split('-')[0])
            upper_bound = int(rule_range.split('-')[1])
            rule_ranges.append((lower_bound, upper_bound))
        return rule_ranges

    def is_valid(self, ticket_field):
        for rule_range in self.ranges:
            if rule_range[0] <= ticket_field <= rule_range[1]:
                return True
        return False


# returns your ticket, all other tickets and all the rules
def get_train_data():
    train_data = [seg.splitlines() for seg in ut.read_input().split('\n\n')]

    # All ticket rules
    rules = []
    for rule in train_data[0]:
        rule = rule.split(': ')
        rule_name = rule[0]
        rule_ranges = rule[1].split(' or ')
        new_rule = TrainRule(rule_name, rule_ranges)
        rules.append(new_rule)

    your_ticket = [int(el) for el in train_data[1][1].split(',')]

    nearby_tickets = []
    for ticket in train_data[2][1:]:
        nearby_tickets.append([int(el) for el in ticket.split(',')])

    return rules, your_ticket, nearby_tickets


def get_error_rate(ticket, train_rules):
    error_rate = 0
    invalid = False
    for ticket_field in ticket:
        if not any([train_rule.is_valid(ticket_field) for train_rule in train_rules]):
            error_rate += ticket_field
            invalid = True
    return error_rate, invalid


def get_valid_tickets(tickets, train_rules):
    valid_tickets = []
    for ticket in tickets:
        error_rate, invalid = get_error_rate(ticket, train_rules)
        if not invalid:
            valid_tickets.append(ticket)
    return valid_tickets


def get_correct_rules(train_rules, ticket_fields):
    correct_rules = []
    for train_rule in train_rules:
        if all([train_rule.is_valid(ticket_field) for ticket_field in ticket_fields]):
            correct_rules.append(train_rule.name)
    return correct_rules


def get_correct_rule_order(valid_tickets, train_rules):
    rule_order_suggestions = []
    for row in range(len(valid_tickets[0])):
        ticket_fields = [valid_ticket[row] for valid_ticket in valid_tickets]
        rule_order_suggestions.append(get_correct_rules(train_rules, ticket_fields))

    taken = {}
    correct_order = {}
    while len(correct_order) < len(train_rules):
        for index in range(len(rule_order_suggestions)):
            rule_row = rule_order_suggestions[index]
            if rule_row:
                if len(rule_row) == 1:
                    rule = rule_row[0]
                    correct_order[index] = rule
                    taken[rule] = True
                    rule_order_suggestions[index] = []
                elif len(rule_row) > 1:
                    new_rule_row = []
                    for rule in rule_row:
                        if not taken.get(rule, False):
                            new_rule_row.append(rule)
                    rule_order_suggestions[index] = new_rule_row
    return correct_order


def part_one():
    train_rules, your_ticket, nearby_tickets = get_train_data()
    error_rate = 0
    for nearby_ticket in nearby_tickets:
        error_rate_ticket, invalid = get_error_rate(nearby_ticket, train_rules)
        error_rate += error_rate_ticket
    ut.print_answer(error_rate)


def part_two():
    train_rules, your_ticket, nearby_tickets = get_train_data()
    valid_tickets = get_valid_tickets(nearby_tickets, train_rules)
    correct_rule_order = get_correct_rule_order(valid_tickets, train_rules)

    answer = 1
    for rule_index in correct_rule_order.keys():
        rule_name = correct_rule_order[rule_index]
        if rule_name.split()[0] == 'departure':
            answer *= your_ticket[rule_index]
    ut.print_answer(answer)

