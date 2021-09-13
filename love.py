from board import Board

board = Board(cols=5, rows=5, rect_size=100)
board.setup(5, "fast")
board.draw()

color = (1, 0, 0)
for row in range(1, 6):
	for col in range(1, 6):
		cond1 = (row == 1 and col%2==0)
		cond2 = (row in (2, 3))
		cond3 = (row == 4 and col in range(2, 5))
		cond4 = (row == 5 and col == 3)
		if cond1 or cond2 or cond3 or cond4:
			board.paint(col, row, color)

Board.done()
