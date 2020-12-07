import ut


class Bag:

    def __init__(self, color, inner_bags):
        self.color = color
        self.inner_bags = inner_bags

    def contains_bag(self, bag_color):
        if self.color == bag_color:
            return True
        else:
            for inner_bag in self.inner_bags:
                inner_bag_color = inner_bag[0]
                if all_bags[inner_bag_color].contains_bag(bag_color):
                    return True
            return False

    def get_held_bags(self):
        held_bags = 0
        if self.inner_bags:
            for inner_bag in self.inner_bags:
                inner_bag_color = inner_bag[0]
                inner_bag_amount = inner_bag[1]
                held_bags += inner_bag_amount*all_bags[inner_bag_color].get_held_bags()
            return held_bags + 1
        else:
            return 1


def get_bags():
    bag_data = [line.split(' contain ') for line in ut.read_input().splitlines()]
    bags = {}
    for bag in bag_data:
        bag_color = bag[0].split(' bags')[0]
        inner_bags = []
        for inner_bag in bag[1].split(', '):
            inner_bag = inner_bag.split()
            if str.isnumeric(inner_bag[0]):
                amount = int(inner_bag[0])
                color = inner_bag[1] + ' ' + inner_bag[2]
                inner_bags.append((color, amount))
        new_bag = Bag(bag_color, inner_bags)
        bags[bag_color] = new_bag
    return bags


all_bags = get_bags()


def part_one():
    count = 0
    for bag in all_bags.keys():
        if not bag == 'shiny gold':
            if all_bags[bag].contains_bag('shiny gold'):
                count += 1
    ut.print_answer(count)


def part_two():
    required_bags = all_bags['shiny gold'].get_held_bags() - 1
    ut.print_answer(required_bags)



