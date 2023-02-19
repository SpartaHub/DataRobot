from argparse import ArgumentParser

from src.letters_grid import LettersGrid
from src.tree import Tree


def get_words_from_one_direction(direction_function, row_number, column_number, roots):
    for letter in direction_function(row_number, column_number):
        children = roots.get_children(letter)
        if children is None:
            break
        if children.get_word():
            yield children.get_word()
        roots = children


def get_words_from_all_directions(grid, words_tree):
    roots = words_tree.root
    for row_number in range(grid.row_numbers):
        for column_number in range(grid.column_numbers):
            for direction_function in grid.get_direction_functions():
                for word in get_words_from_one_direction(direction_function, row_number, column_number, roots):
                    yield word


def run():
    parser = ArgumentParser(description="WordSearchRunner")
    parser.add_argument("--words_dict", dest="words_dict", required=True,
                        help="File with words which should be searched")
    parser.add_argument("--rows", dest="number_rows", default=15, help="The number of the rows on the board")
    parser.add_argument("--columns", dest="number_columns", default=15, help="The number of the columns on the board")
    args = parser.parse_args()

    words_tree = Tree(args.words_dict)
    grid = LettersGrid(int(args.number_rows), int(args.number_columns))
    grid.create_grid()
    grid.print_grid()

    for word in get_words_from_all_directions(grid, words_tree):
        print(word)


if __name__ == '__main__':
    run()
