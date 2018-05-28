from numpy.random import choice

m = 31
n = 16
mines = 99


class Field:
    def __init__(self, first_step):
        self.field = [[0] * m for _ in range(n)]
        mines_positions = list(range(88)) + [5 * 31 + 12, 8 * 31 + 13 - 1, 9 * 31 + 13 - 1, 4 * 31 + 15, 10 * 31 + 16 - 1, 4 * 31 + 18, 5 * 31 + 18, 7 * 31 + 18 - 1, 8 * 31 + 18 - 1, 10 * 31 + 18 - 1, 4 * 31 + 17]#choice(m * n - 1, mines)
        for pos in mines_positions:
            # try:
            self.field[(pos + (pos > first_step)) // m][(pos + (pos > first_step)) % m] = -1
            # except IndexError:
            #     print(pos)
            #     print((pos + (pos > first_step)) // n, (pos + (pos > first_step)) % m)
        for i in range(n):
            for j in range(m):
                if self.field[i][j] != -1:
                    self.field[i][j] = self.mines_around(j, i)

    def mines_around(self, x, y):
        return sum([sum([x + i >= 0 and x + i < m and y + j >= 0 and y + j < n and self.field[y + j][x + i] == -1 for i in [-1, 0, 1]]) for j in [-1, 0, 1]])

    def print(self):
        for i in range(n):
            for j in range(m):
                print('{}'.format(self.field[i][j]).ljust(3), end='')
            print()

    def get(self, x, y):
        return self.field[y][x]

#
# field = Field(7 * 31 + 15)
# field.print()