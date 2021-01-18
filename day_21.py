import ut


class Food:

    def __init__(self, ingredients, allergens):
        self.ingredients = ingredients
        self.allergens = allergens


def get_food_data():
    food_data = [line.replace('(', '').replace(')', '').replace(',', '').split() for line in ut.read_input().splitlines()]
    food = []
    for food_item in food_data:
        ingredients = []
        allergens = []
        is_allergen = False
        for item in food_item:
            if item == 'contains':
                is_allergen = True
                continue

            if not is_allergen:
                ingredients.append(item)
            else:
                allergens.append(item)
        food.append(Food(ingredients, allergens))
    return food


def get_all_ingredients(foods):
    ingredients = []
    for food in foods:
        ingredients += food.ingredients
    return list(dict.fromkeys(ingredients).keys())


def get_all_allergens(foods):
    allergens = []
    for food in foods:
        allergens += food.allergens
    return list(dict.fromkeys(allergens).keys())


def get_possible_allergens(foods):
    all_allergens = get_all_allergens(foods)
    all_ingredients = get_all_ingredients(foods)
    possible_allergens = {}
    for allergen in all_allergens:
        possible_allergens[allergen] = dict.fromkeys(all_ingredients, 0)

    for food in foods:
        for allergen in food.allergens:
            for ingredient in food.ingredients:
                possible_allergens[allergen][ingredient] += 1

    return possible_allergens


def get_allergens(possible_allergens: dict):

    allergens = {}

    while possible_allergens.keys():
        current_allergens = list(possible_allergens.keys()).copy()
        for allergen in current_allergens:
            ingredients = possible_allergens[allergen]
            max_votes = 0
            contestants = []
            for ingredient in ingredients.keys():
                if ingredient not in allergens.keys():
                    votes = ingredients[ingredient]
                    if votes > max_votes:
                        max_votes = votes
                        contestants = [ingredient]
                    elif votes == max_votes:
                        contestants.append(ingredient)

            if len(contestants) == 1:
                ingredient = contestants[0]
                allergens[ingredient] = allergen
                possible_allergens.pop(allergen)

    return allergens


def get_non_allergens(allergens, ingredients):
    non_allergens = []
    for ingredient in ingredients:
        if ingredient not in allergens.keys():
            non_allergens.append(ingredient)
    return non_allergens


def count_non_allergen_occurrences(foods, non_allergens):
    count = 0
    for food in foods:
        for ingredient in food.ingredients:
            if ingredient in non_allergens:
                count += 1
    return count


def print_canonical_dangerous_list(allergens: dict):
    print(allergens.values())
    print(allergens)
    for ingredient in allergens.keys():
        print(ingredient, end=',')


def part_one():
    foods = get_food_data()
    possible_allergens = get_possible_allergens(foods)
    allergens = get_allergens(possible_allergens)
    non_allergens = get_non_allergens(allergens, get_all_ingredients(foods))
    answer = count_non_allergen_occurrences(foods, non_allergens)
    ut.print_answer(answer)


def part_two():
    foods = get_food_data()
    possible_allergens = get_possible_allergens(foods)
    allergens = get_allergens(possible_allergens)
    print_canonical_dangerous_list(allergens)


part_two()

