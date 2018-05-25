from field import Field, m, n, mines


class Solver:
    def __init__(self):
        self.field = Field(m * n // 2 + m // 2)
        self.opened_part = [[-2] * m for _ in range(n)]
        self.opened_part[n // 2][m // 2] = self.field.get(m // 2, n // 2)
        self.unsolved_ceils = set()
        self.expand(m // 2, n // 2)

    def expand(self, x, y):
        if self.opened_part[y][x] == 0:
            for i in -1, 0, 1:
                for j in -1, 0, 1:
                    if x + i >= 0 and x + i < m and y + j >= 0 and y + j < n and self.opened_part[y + j][x + i] == -2:
                        self.opened_part[y + j][x + i] = self.field.get(x + i, y + j)
                        self.expand(x + i, y + j)
        else:
            self.unsolved_ceils.add((x, y))

    def print(self):
        for i in range(n):
            for j in range(m):
                print('{}'.format(self.opened_part[i][j]).ljust(3), end='')
            print()

    def unopened_around(self, x, y):
        return sum([sum(
            [x + i >= 0 and x + i < m and y + j >= 0 and y + j < n and self.opened_part[y + j][x + i] == -2 for i in
             [-1, 0, 1]]) for j in [-1, 0, 1]])

    def mines_around(self, x, y):
        return sum([sum(
            [x + i >= 0 and x + i < m and y + j >= 0 and y + j < n and self.opened_part[y + j][x + i] == -3 for i in
             [-1, 0, 1]]) for j in [-1, 0, 1]])

    def obvious_opening(self):
        while True:
            break_after_for = True
            for ceil in self.unsolved_ceils:

                x, y = ceil
                unopened = self.unopened_around(x, y)
                mines_around = self.mines_around(x, y)
                value = self.opened_part[y][x]
                if unopened == value - mines_around: # open all ceils
                    for i in -1, 0, 1:
                        for j in -1, 0, 1:
                            if x + i >= 0 and x + i < m and y + j >= 0 and y + j < n and self.opened_part[y + j][x + i] == -2:
                                self.opened_part[y + j][x + i] = self.field.get(x + i, y + j)
                                self.unsolved_ceils.add((x + i, y + j))
                    self.unsolved_ceils.remove(ceil)
                    break_after_for = False
                    break
                elif mines_around == value: #mark all unopened as mines (-3)
                    for i in -1, 0, 1:
                        for j in -1, 0, 1:
                            if x + i >= 0 and x + i < m and y + j >= 0 and y + j < n and self.opened_part[y + j][x + i] == -2:
                                self.opened_part[y + j][x + i] = -3
                    self.unsolved_ceils.remove(ceil)
                    break_after_for = False
                    break
            if break_after_for:
                break

s = Solver()
s.print()
s.obvious_opening()
s.print()
# s.field.print()