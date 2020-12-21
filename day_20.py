import ut
import math
import copy

sea_monster = [list(line) for line in ut.read_file('sea_monster.txt').splitlines()]


class Piece:

    def __init__(self, piece_id, image):
        self.image = image
        self.piece_id = piece_id

    def up_edge(self):
        return self.image[0]

    def down_edge(self):
        return self.image[-1]

    def left_edge(self):
        return [row[0] for row in self.image]

    def right_edge(self):
        return [row[-1] for row in self.image]

    def flip(self):
        for row in self.image:
            row.reverse()

    def rotate(self):
        self.image = [[row[i] for row in self.image] for i in range(len(self.image))]
        self.flip()

    def remove_border(self):
        self.image = [row[1:-1] for row in self.image[1:-1]]

    def print_piece(self):
        for row in self.image:
            for char in row:
                print(char, end='')
            print()
        print()

    def count_hashtags(self):
        count = 0
        for row in self.image:
            count += row.count('#')
        return count


class Puzzle:

    def __init__(self, lose_pieces: list):
        self.attached_pieces = {}
        self.open_positions = [(0, 0)]
        self.lose_pieces = lose_pieces

    def match_(self, piece, pos):
        # up
        up_piece = self.attached_pieces.get((pos[0], pos[1] - 1), 'empty')
        if not up_piece == 'empty' and not piece.up_edge() == up_piece.down_edge():
            return False

        # down
        down_piece = self.attached_pieces.get((pos[0], pos[1] + 1), 'empty')
        if not down_piece == 'empty' and not piece.down_edge() == down_piece.up_edge():
            return False

        # left
        left_piece = self.attached_pieces.get((pos[0] - 1, pos[1]), 'empty')
        if not left_piece == 'empty' and not piece.left_edge() == left_piece.right_edge():
            return False

        # right
        right_piece = self.attached_pieces.get((pos[0] + 1, pos[1]), 'empty')
        if not right_piece == 'empty' and not piece.right_edge() == right_piece.left_edge():
            return False

        return True

    def match(self, piece, pos):

        for i in range(4):
            if self.match_(piece, pos):
                return True
            else:
                piece.rotate()

        piece.flip()

        for i in range(4):
            if self.match_(piece, pos):
                return True
            else:
                piece.rotate()

        return False

    def attach(self, piece, pos):
        if self.match(piece, pos):
            self.lose_pieces.remove(piece)
            self.open_positions.remove(pos)
            self.attached_pieces[pos] = piece
            neighbor_positions = ut.udlr_neighbours(pos)
            for neighbor_pos in neighbor_positions:
                if self.attached_pieces.get(neighbor_pos, 'empty') == 'empty':
                    self.open_positions.append(neighbor_pos)
            return True
        return False

    def assemble(self):

        while self.lose_pieces:
            for piece_to_attach in self.lose_pieces:
                for open_pos in self.open_positions:
                    attached = self.attach(piece_to_attach, open_pos)
                    if attached:
                        break

    def get_corner_pieces(self):
        min_x = min([pos[0] for pos in self.attached_pieces])
        max_x = max([pos[0] for pos in self.attached_pieces])
        min_y = min([pos[1] for pos in self.attached_pieces])
        max_y = max([pos[1] for pos in self.attached_pieces])

        top_l = self.attached_pieces[(min_x, min_y)].piece_id
        top_r = self.attached_pieces[(max_x, min_y)].piece_id
        bot_l = self.attached_pieces[(min_x, max_y)].piece_id
        bot_r = self.attached_pieces[(max_x, max_y)].piece_id

        return top_l, top_r, bot_l, bot_r

    def merge_image_pieces(self):

        image_pieces = list(self.attached_pieces.values())
        for image_piece in image_pieces:
            image_piece.remove_border()

        merged_image = []
        puzzle_dim = int(math.sqrt(len(self.attached_pieces.keys())))
        piece_dim = len(image_pieces[0].image[0])
        for row in range(puzzle_dim * piece_dim):
            merged_image.append([])

        min_x = min([pos[0] for pos in self.attached_pieces])
        max_x = max([pos[0] for pos in self.attached_pieces])
        min_y = min([pos[1] for pos in self.attached_pieces])
        max_y = max([pos[1] for pos in self.attached_pieces])

        row_offset = 0
        for row in range(min_y, max_y + 1):
            merged_image_row = row_offset * piece_dim

            for col in range(min_x, max_x + 1):
                piece = self.attached_pieces[(col, row)]
                for image_row in range(0, piece_dim):
                    merged_image[merged_image_row + image_row] += piece.image[image_row]

            row_offset += 1

        return Piece(0, merged_image)


def get_puzzle_pieces():
    puzzle_pieces = []
    image_pieces = [[list(line) for line in el.splitlines()] for el in ut.read_input().split('\n\n')]
    for image_piece in image_pieces:
        tile_id = ''.join(image_piece[0]).split()[1][0:-1]
        tile_image = image_piece[1:]
        new_piece = Piece(tile_id, tile_image)
        puzzle_pieces.append(new_piece)
    return puzzle_pieces


def match_sea_monster(image_piece: Piece):
    image = image_piece.image
    sea_monster_count = 0
    sea_monster_height = 3
    sea_monster_width = 20
    for row in range(len(image) - sea_monster_height):
        for col in range(len(image[0]) - sea_monster_width):
            match = True

            for i in range(sea_monster_height):
                image_row = ''.join(image[row + i][col:col + len(sea_monster[i])])
                sea_monster_row = sea_monster[i]
                for index in range(len(image_row)):
                    if sea_monster_row[index] == '#':
                        if not image_row[index] == '#':
                            match = False
            if match:
                sea_monster_count += 1
    return image_piece.count_hashtags() - 15 * sea_monster_count


def part_one():
    puzzle = Puzzle(get_puzzle_pieces())
    puzzle.assemble()
    answer = 1
    for tile_id in puzzle.get_corner_pieces():
        answer *= int(tile_id)
    ut.print_answer(answer)


def part_two():
    puzzle = Puzzle(get_puzzle_pieces())
    puzzle.assemble()
    final_image = puzzle.merge_image_pieces()
    answer = math.inf
    for i in range(4):
        answer = min(match_sea_monster(copy.copy(final_image)), answer)
        final_image.rotate()
    final_image.flip()
    for i in range(4):
        answer = min(match_sea_monster(copy.copy(final_image)), answer)
        final_image.rotate()
    ut.print_answer(answer)

