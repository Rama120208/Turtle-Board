import turtle

class Board:
	
	def __init__(self, cols=5, rows=5, pos=(0,0), rect_size=50, color=(0, 0, 0), background_color=(255, 255, 255)):
		"""
		cols: total column of board.
		rows: total row of board.
		pos: (x, y) position for board center.
		rect_size: size every rect, both width and height.
		color: color of board's line, can be color hex string, color name, or rgb color.
		background_color: background of the board, can be color hex string, color name, or rgb color.
		"""
		if cols < 1 or rows < 1:
			raise ValueError("Cols and rows must be higher than 0!")
		elif rect_size < 1:
			raise ValueError("Rect size must be higher than 0!")
		self.__pen = turtle.Turtle()
		self.__cols = cols
		self.__rows = rows
		self.__pos = pos
		self.__rect_size = rect_size
		self.__color = color
		self.__background_color = background_color
		self.__isdrawed = False
		self.__pen.pencolor(color)

	def setup(self, pensize, speed):
		"""
		pensize: size of pen.
		speed: speed of pen, can be speed string or int. speed args can be viewed at turtle documentation.
		"""
		self.__pen.pensize(pensize)
		self.__pen.speed(speed)

	def draw(self):
		width = self.__cols*self.__rect_size
		height = self.__rows*self.__rect_size
		x = self.__pos[0] - width/2
		y = self.__pos[1] - height/2
		
		#Setup
		self.__pen.up()
		self.__pen.goto(x, y)
		self.__pen.down()
		
		#Draw outer line
		self.__pen.color(self.__color, self.__background_color)
		self.__pen.begin_fill()
		for _ in range(0, 2):
			self.__pen.forward(width)
			self.__pen.left(90)
			self.__pen.forward(height)
			self.__pen.left(90)
		self.__pen.end_fill()
		
		#Draw inner line
		self.__pen.left(90)
		x_inner = x
		for _ in range(0, self.__cols-1):
			x_inner += self.__rect_size
			self.__pen.up()
			self.__pen.goto(x_inner, y)
			self.__pen.down()
			self.__pen.forward(height)
		self.__pen.right(90)
		y_inner = y
		for _ in range(0, self.__rows-1):
			y_inner += self.__rect_size
			self.__pen.up()
			self.__pen.goto(x, y_inner)
			self.__pen.down()
			self.__pen.forward(width)
			
		self.__isdrawed = True
		self.__pen.hideturtle()
			
	def paint(self, col, row, color):
		"""
		! CAN BE USED AFTER CALL `draw()` METHOD !
		------
		col: column position to paint.
		row: row position to paint.
		color: color used to fill rect, can be can be color hex string, color name, or rgb color.
		------
		Column and row have first index (1, 1) at top-left board.
		To make a horizontal line, you can use loop to increase col argument.
		"""
		if col < 1 or row < 1:
			raise ValueError("Cols and rows must be higher than 0!")
		elif not self.__isdrawed:
			raise SyntaxError("Can be used after call `draw()` method")
		self.__pen.speed(0)
			
		width = self.__cols*self.__rect_size
		height = self.__rows*self.__rect_size
		x = self.__pos[0] - width/2 + (col-1)*self.__rect_size
		y = self.__pos[1] + height/2 - (row-1)*self.__rect_size
		
		#Setup position
		self.__pen.up()
		self.__pen.goto(x, y)
		self.__pen.down()
		
		#Filling rect
		self.__pen.color(self.__color, color)
		self.__pen.begin_fill()
		for _ in range(4):
			self.__pen.forward(self.__rect_size)
			self.__pen.right(90)
		self.__pen.end_fill()

	@staticmethod
	def done():
		"""
		! MUST BE CALLED ONCE AT THE END OF PROGRAM AFTER USING THIS CLASS !
		"""
		turtle.mainloop()
