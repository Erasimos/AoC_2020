import ut

decks = [[int(el) for el in deck.splitlines()] for deck in ut.read_input().split("\n\n")]
deck1 = decks[0]
deck2 = decks[1]


class CombatGame:

    def __init__(self, deck1, deck2):
        self.deck1 = deck1
        self.deck2 = deck2

    def play_turn(self):
        card_1 = self.deck1[0]
        card_2 = self.deck2[0]

        if card_1 > card_2:
            self.deck1 = self.deck1[1:] + [card_1] + [card_2]
            self.deck2 = self.deck2[1:]
        elif card_2 > card_1:
            self.deck2 = self.deck2[1:] + [card_2] + [card_1]
            self.deck1 = self.deck1[1:]

    def calc_score(self):
        winning_deck = self.deck1 if self.deck1 else self.deck2
        winning_deck.reverse()
        return sum([winning_deck[i] * (i + 1) for i in range(len(winning_deck))])

    def play(self):
        while self.deck1 and self.deck2:
            self.play_turn()
        return self.calc_score()


class RecursiveCombatGame:

    def __init__(self, players):
        self.players = players
        self.states = {self.get_state(): True}

    def get_state(self):
        return "".join([str(el) + "," for el in self.players["player_1"]]) + \
               "".join([str(el) for el in self.players["player_2"]])

    def play_turn(self):
        card_1 = self.players["player_1"][0]
        card_2 = self.players["player_2"][0]
        deck_1 = self.players["player_1"][1:]
        deck_2 = self.players["player_2"][1:]

        if len(deck_1) >= card_1 and len(deck_2) >= card_2:
            new_deck_1 = deck_1[0:card_1]
            new_deck_2 = deck_2[0:card_2]
            recursive_game = RecursiveCombatGame({"player_1": new_deck_1, "player_2": new_deck_2})
            winner, loser = recursive_game.play()

        elif card_1 > card_2:
            winner = "player_1"
            loser = "player_2"

        else:
            winner = "player_2"
            loser = "player_1"

        winning_card = card_1 if winner == "player_1" else card_2
        losing_card = card_1 if not winner == "player_1" else card_2
        self.players[winner] = self.players[winner][1:] + [winning_card] + [losing_card]
        self.players[loser] = self.players[loser][1:]

    def calc_score(self, winner):
        winning_deck = self.players[winner]
        winning_deck.reverse()
        return sum([winning_deck[i] * (i + 1) for i in range(len(winning_deck))])

    def play(self):
        while all(list(self.players.values())):
            self.play_turn()
            new_state = self.get_state()

            if self.states.get(new_state, False):
                return "player_1", "player_2"
            else:
                self.states[new_state] = True

        winner = "player_1" if self.players["player_1"] else "player_2"
        loser = "player_1" if not self.players["player_1"] else "player_2"
        return winner, loser


def part_one():
    combat_game = CombatGame(deck1, deck2)
    ut.print_answer(combat_game.play())


def part_two():
    recursive_combat_game = RecursiveCombatGame({"player_1": deck1, "player_2": deck2})
    winner, loser = recursive_combat_game.play()
    ut.print_answer(recursive_combat_game.calc_score(winner))


part_two()



