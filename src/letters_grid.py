import random
import string


class LettersGrid:

    def __init__(self, row_numbers, column_numbers):
        self.row_numbers = row_numbers
        self.column_numbers = column_numbers
        self.grid = []

    def create_grid(self):
        for row_number in range(self.row_numbers):
            row = random.choices(string.ascii_lowercase, k=self.column_numbers)
            self.grid.append(row)

    def get_grid(self):
        return self.grid

    def move_forward(self, row_number, column_number):
        for column in range(column_number, self.column_numbers, 1):
            yield self.get_grid()[row_number][column]

    def move_backward(self, row_number, column_number):
        for column in range(column_number, -1, -1):
            yield self.get_grid()[row_number][column]

    def move_downward(self, row_number, column_number):
        for row in range(row_number, self.row_numbers):
            yield self.get_grid()[row][column_number]

    def move_upward(self, row_number, column_number):
        for row in range(row_number, -1, -1):
            yield self.get_grid()[row][column_number]

    def move_forward_downward(self, row_number, column_number):
        while row_number != self.row_numbers and column_number != self.column_numbers:
            yield self.get_grid()[row_number][column_number]
            row_number += 1
            column_number += 1

    def move_forward_upward(self, row_number, column_number):
        while row_number != -1 and column_number != self.column_numbers:
            yield self.get_grid()[row_number][column_number]
            column_number += 1
            row_number -= 1

    def move_backward_downward(self, row_number, column_number):
        while row_number != self.row_numbers and column_number != -1:
            yield self.get_grid()[row_number][column_number]
            row_number += 1
            column_number -= 1

    def move_backward_upward(self, row_number, column_number):
        while row_number != -1 and column_number != -1:
            yield self.get_grid()[row_number][column_number]
            row_number -= 1
            column_number -= 1

    def get_direction_functions(self):
        return [self.move_forward, self.move_backward, self.move_downward, self.move_upward, self.move_forward_downward,
                self.move_forward_upward, self.move_backward_downward, self.move_backward_upward]

    def print_grid(self):
        for row in self.get_grid():
            print(row)
