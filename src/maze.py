from draw import Cell
from time import sleep
import random


class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed is not None:
            random.seed(seed)

        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self._solve()

    def _create_cells(self):
        for x in range(self._num_cols):
            col = []
            for y in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return

        cell = self._cells[i][j]
        x1 = self._x1 + self._cell_size_x * i
        y1 = self._y1 + self._cell_size_y * j
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        cell.draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return

        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance_x = 0
        entrance_y = 0
        self._cells[entrance_x][entrance_y].has_top_wall = False
        self._draw_cell(entrance_x, entrance_y)

        exit_x = self._num_cols - 1
        exit_y = self._num_rows - 1
        self._cells[exit_x][exit_y].has_bottom_wall = False
        self._draw_cell(exit_x, exit_y)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_visit = []

            # top
            if j > 0 and self._cells[i][j-1].visited is False:
                to_visit.append((i, j-1))

            # right
            if i < self._num_cols - 1 and self._cells[i+1][j].visited is False:
                to_visit.append((i+1, j))

            # bottom
            if j < self._num_rows - 1 and self._cells[i][j+1].visited is False:
                to_visit.append((i, j+1))

            # left
            if i > 0 and self._cells[i-1][j].visited is False:
                to_visit.append((i-1, j))

            if len(to_visit) < 1:
                self._draw_cell(i, j)
                return

            random_visit_index = random.randrange(0, len(to_visit))
            random_i, random_j = to_visit[random_visit_index]

            # top
            if random_j < j:
                self._cells[i][j].has_top_wall = False
                self._cells[random_i][random_j].has_bottom_wall = False

            # right
            if random_i > i:
                self._cells[i][j].has_right_wall = False
                self._cells[random_i][random_j].has_left_wall = False

            # bottom
            if random_j > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[random_i][random_j].has_top_wall = False

            # left
            if random_i < i:
                self._cells[i][j].has_left_wall = False
                self._cells[random_i][random_j].has_right_wall = False

            self._break_walls_r(random_i, random_j)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def _solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        current = self._cells[i][j]
        current.visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        # top
        if j > 0:
            top_cell = self._cells[i][j-1]

            if (
                top_cell.visited is False
                and current.has_top_wall is False
            ):
                current.draw_move(top_cell)
                output = self._solve_r(i, j-1)
                if output is True:
                    return True
                current.draw_move(top_cell, undo=True)

        # right
        if i < self._num_cols - 1:
            right_cell = self._cells[i+1][j]

            if (
                right_cell.visited is False
                and current.has_right_wall is False
            ):
                current.draw_move(right_cell)
                output = self._solve_r(i+1, j)
                if output is True:
                    return True
                current.draw_move(right_cell, undo=True)

        # bottom
        if j < self._num_rows - 1:
            bottom_cell = self._cells[i][j+1]

            if (
                bottom_cell.visited is False
                and current.has_bottom_wall is False
            ):
                current.draw_move(bottom_cell)
                output = self._solve_r(i, j+1)
                if output is True:
                    return True
                current.draw_move(bottom_cell, undo=True)

        # left
        if i > 0:
            left_cell = self._cells[i-1][j]

            if (
                left_cell.visited is False
                and current.has_left_wall is False
            ):
                current.draw_move(left_cell)
                output = self._solve_r(i-1, j)
                if output is True:
                    return True
                current.draw_move(left_cell, undo=True)

        return False
