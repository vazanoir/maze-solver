import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        # test multiple sizes
        cols_and_rows_list = [(12, 10), (5, 5), (100, 400)]
        for cols_and_rows in cols_and_rows_list:
            num_cols = cols_and_rows[0]
            num_rows = cols_and_rows[1]
            m = Maze(0, 0, num_rows, num_cols, 10, 10)

            self.assertEqual(len(m._cells), num_cols)
            self.assertEqual(len(m._cells[0]), num_rows)

        # test empty
        num_cols = 0
        num_rows = 0
        m = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(len(m._cells), 0)


if __name__ == "__main__":
    unittest.main()
