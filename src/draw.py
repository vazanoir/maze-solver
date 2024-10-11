class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x,
            self.p1.y,
            self.p2.x,
            self.p2.y,
            fill=fill_color,
            width=2
        )


class Cell():
    def __init__(self, win=None):
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.__win = win

    def draw(self, x1, y1, x2, y2):
        if self.__win is None:
            return

        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        self.__draw_top_wall(x1, y1, x2, y2, "white")
        self.__draw_right_wall(x1, y1, x2, y2, "white")
        self.__draw_bottom_border(x1, y1, x2, y2, "white")
        self.__draw_left_border(x1, y1, x2, y2, "white")

        if self.has_top_wall:
            self.__draw_top_wall(x1, y1, x2, y2)
        if self.has_right_wall:
            self.__draw_right_wall(x1, y1, x2, y2)
        if self.has_bottom_wall:
            self.__draw_bottom_border(x1, y1, x2, y2)
        if self.has_left_wall:
            self.__draw_left_border(x1, y1, x2, y2)

    def __draw_top_wall(self, x1, y1, x2, y2, fill_color="black"):
        line = Line(Point(x1, y1), Point(x2, y1))
        self.__win.draw_line(line, fill_color)

    def __draw_right_wall(self, x1, y1, x2, y2, fill_color="black"):
        line = Line(Point(x2, y1), Point(x2, y2))
        self.__win.draw_line(line, fill_color)

    def __draw_bottom_border(self, x1, y1, x2, y2, fill_color="black"):
        line = Line(Point(x1, y2), Point(x2, y2))
        self.__win.draw_line(line, fill_color)

    def __draw_left_border(self, x1, y1, x2, y2, fill_color="black"):
        line = Line(Point(x1, y1), Point(x1, y2))
        self.__win.draw_line(line, fill_color)

    def draw_move(self, to_cell, undo=False):
        line = Line(
            Point(
                (self.__x1 + self.__x2) / 2,
                (self.__y1 + self.__y2) / 2
            ),
            Point(
                (to_cell.__x1 + to_cell.__x2) / 2,
                (to_cell.__y1 + to_cell.__y2) / 2
            )
        )

        color = "red"
        if undo:
            color = "gray"

        self.__win.draw_line(line, color)
