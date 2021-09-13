from board import Board

FILL_COLOR = "hotpink"
BACKGROUND_COLOR = "steelblue"
board = Board(cols=13, rows=7,  background_color=BACKGROUND_COLOR)
board.setup(5, 0)
board.draw()

for row in range(1, 8):
	for col in range(1, 14):
		cond1 = (row in range(2, 7) and col == 2)
		cond2 = (row == 2 and col in [5, 7])
		cond3 = (row in [3, 4] and col in range(4, 9))
		cond4 = (row == 5 and col in range(5, 8))
		cond5 = (row == 6 and col == 6)
		cond6 = (row in range(2, 6) and col in [10, 12])
		cond7 = (row == 6 and col in range(10, 13))
		if cond1 or cond2 or cond3 or cond4 or cond5 or cond6 or cond7:
			board.paint(col, row, FILL_COLOR)

Board.done()
