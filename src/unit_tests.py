import tempfile
import unittest
from collections import defaultdict

from src.letters_grid import LettersGrid
from src.runner import get_words_from_all_directions
from src.tree import Tree

GRID = [["a", "a", "b", "a", "d"],
        ["d", "o", "u", "s", "y"],
        ["c", "i", "m", "l", "j"],
        ["z", "p", "r", "e", "n"],
        ["x", "f", "k", "g", "b"]]

WORDS_PRESENT = {"aab": 1, "usy": 1, "pre": 1, "aomeb": 1, 'kpc': 1, 'cob': 1, 'jek': 1, 'bum': 1, 'krm': 1}
WORDS_ABSENT = ["bada", "axz", "zxa", "zne"]


class TestGridMovingAndSearch(unittest.TestCase):

    def setUp(self):
        self.grid = LettersGrid(len(GRID), len(GRID[0]))
        self.grid.get_grid = lambda: GRID
        self.first_row = self.first_column = 0
        self.last_row = len(GRID) - 1

    def test_move_forward(self):
        expected = [["a", "a", "b", "a", "d"],
                    ["a", "b", "a", "d"],
                    ["b", "a", "d"],
                    ["a", "d"],
                    ["d"]]

        for column_number in range(self.grid.column_numbers):
            actual = list(self.grid.move_forward(self.first_row, column_number))
            self.assertEqual(actual, expected[column_number],
                             "actual: {}\nexpected: {}".format(actual, expected[column_number]))

    def test_move_backward(self):
        expected = [["a"],
                    ["a", "a"],
                    ["b", "a", "a"],
                    ["a", "b", "a", "a"],
                    ["d", "a", "b", "a", "a"]]

        for column_number in range(self.grid.column_numbers):
            actual = list(self.grid.move_backward(self.first_row, column_number))
            self.assertEqual(actual, expected[column_number],
                             "actual: {}\nexpected: {}".format(actual, expected[column_number]))

    def test_move_downward(self):
        expected = [["a", "d", "c", "z", "x"],
                    ["d", "c", "z", "x"],
                    ["c", "z", "x"],
                    ["z", "x"],
                    ["x"]]
        for row_number in range(self.grid.row_numbers):
            actual = list(self.grid.move_downward(row_number, self.first_column))
            self.assertEqual(actual, expected[row_number],
                             "actual: {}\nexpected: {}".format(actual, expected[row_number]))

    def test_move_upward(self):
        expected = [["a"],
                    ["d", "a"],
                    ["c", "d", "a"],
                    ["z", "c", "d", "a"],
                    ["x", "z", "c", "d", "a"]]

        for row_number in range(self.grid.row_numbers):
            actual = list(self.grid.move_upward(row_number, self.first_column))
            self.assertEqual(actual, expected[row_number],
                             "actual: {}\nexpected: {}".format(actual, expected[row_number]))

    def test_move_forward_downward(self):
        expected = [["a", "o", "m", "e", "b"],
                    ["a", "u", "l", "n"],
                    ["b", "s", "j"],
                    ["a", "y"],
                    ["d"]]

        for column_number in range(self.grid.column_numbers):
            actual = list(self.grid.move_forward_downward(self.first_row, column_number))
            self.assertEqual(actual, expected[column_number],
                             "actual: {}\nexpected: {}".format(actual, expected[column_number]))

    def test_move_forward_upward(self):
        expected = [["a"],
                    ["d", "a"],
                    ["c", "o", "b"],
                    ["z", "i", "u", "a"],
                    ["x", "p", "m", "s", "d"]]

        for row_number in range(self.grid.row_numbers):
            actual = list(self.grid.move_forward_upward(row_number, self.first_column))
            self.assertEqual(actual, expected[row_number],
                             "actual: {}\nexpected: {}".format(actual, expected[row_number]))

    def test_move_backward_downward(self):
        expected = [["a"],
                    ["a", "d"],
                    ["b", "o", "c"],
                    ["a", "u", "i", "z"],
                    ["d", "s", "m", "p", "x"]]

        for column_number in range(self.grid.column_numbers):
            actual = list(self.grid.move_backward_downward(self.first_row, column_number))
            self.assertEqual(actual, expected[column_number],
                             "actual: {}\nexpected: {}".format(actual, expected[column_number]))

    def test_move_backward_upward(self):
        expected = [["x"],
                    ["f", "z"],
                    ["k", "p", "c"],
                    ["g", "r", "i", "d"],
                    ["b", "e", "m", "o", "a"]]

        for column_number in range(self.grid.column_numbers):
            actual = list(self.grid.move_backward_upward(self.last_row, column_number))
            self.assertEqual(actual, expected[column_number],
                             "actual: {}\nexpected: {}".format(actual, expected[column_number]))


class TestWordSearch(unittest.TestCase):
    def setUp(self):
        tmp_file = tempfile.NamedTemporaryFile(mode='w+t')
        for word in WORDS_PRESENT:
            tmp_file.writelines("{}\n".format(word))
        tmp_file.seek(0)

        self.words_tree = Tree(tmp_file.name)
        self.grid = LettersGrid(len(GRID), len(GRID[0]))
        self.grid.get_grid = lambda: GRID

    def test_search(self):
        words_count = defaultdict(int)
        for word in get_words_from_all_directions(self.grid, self.words_tree):
            words_count[word] += 1
        for word, expected_number in WORDS_PRESENT.items():
            actual_number = words_count.get(word, 0)
            self.assertEqual(expected_number, actual_number,
                             "actual: {}\nexpected: {}".format(actual_number, expected_number))
        for word in WORDS_ABSENT:
            self.assertNotIn(word, words_count,
                             "actual: the word '{}' is present in the search result\n"
                             "expected: the word '{}' should not present in the search result".format(word, word))
