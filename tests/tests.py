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

    def test_maze_entrance_and_exit(self):
        num_rows = 5
        num_cols = 5
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(m._cells[0][0].has_top_wall)
        self.assertFalse(m._cells[num_rows - 1][num_cols - 1].has_bottom_wall)


if __name__ == "__main__":
    unittest.main()
