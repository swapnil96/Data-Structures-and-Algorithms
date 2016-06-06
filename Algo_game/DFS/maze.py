import Tkinter
import random
import sys
import numpy
import time

White = 0
Gray = 1
Black = 2

class Maze:
	
	def __init__(self, height, width, size):
		'''Initialize maze'''

		if size < 3:
			raise Exception('Cells must be at least 3 pixels wide')

		self.height = height
		self.width = width
		self.size = size
		self.numrows = height/size
		self.numcols = width/size
		self.master = Tkinter.Tk()
		self.w = Tkinter.Canvas(self.master, width = self.width + 10, height = self.height + 10)
		self.w.pack()
		self.construct()

	def view(self, a = 0):
		'''Show window with maze'''

		#master = Tkinter.Tk()
		#w = Tkinter.Canvas(self.master, width = self.width + 10, height = self.height + 10)
		#self.w.pack()
		self.w.update()
		offset = 5
		self.w.create_line(offset, offset, offset, offset + self.height)
		self.w.create_line(offset, offset, offset + (self.width/self.size/2)*self.size, offset)
		self.w.create_line(offset + self.size*(1 + (self.width/self.size)/2), offset, offset + (self.width/self.size)*self.size, offset)
		for r in xrange(self.numrows):
			for c in xrange(self.numcols):
				if self.hasSouthWall[r, c]:
					self.w.create_line(offset + c*self.size, offset + (r + 1)*self.size, offset + (c + 1)*self.size, offset + (r + 1)*self.size)
				
				if self.hasEastWall[r, c]:
					self.w.create_line(offset + (c + 1)*self.size, offset + r*self.size, offset + (c + 1)*self.size, offset + (r + 1)*self.size)

		#Tkinter.mainloop()
		if a == 1:
			Tkinter.mainloop()

		else:	
			self.w.update()
			time.sleep(0.1)
			self.w.delete('all')
		#w.after(10, lambda:master.destroy())			
		#master.destroy()


	def ClearWall(self, fromCell, toCell):
		'''Remove wall between two cells'''

		if fromCell[1] == toCell[1]:
			self.hasSouthWall[min(fromCell[0], toCell[0]), fromCell[1]] = False

		else:
			self.hasEastWall[fromCell[0], min(fromCell[1], toCell[1])] = False

	def dfsVisit(self, sq):
		'''Conduct DFS search to build maze'''

		while len(self.neighbour[sq]) > 0:
			cell = random.choice(self.neighbour[sq])
			self.neighbour[sq].remove(cell)
			if self.colour[cell] == White:
				self.ClearWall(sq, cell)
				self.dfsVisit(cell)

		self.colour[sq] = Black

	def dfsVisit_nr(self, sq):
		'''Conduct Non Recursive DFS search to build maze'''			

		path = [sq]
		self.colour[sq] = Gray
		while len(path) > 0:
			#print path
			self.view()
			sq = path[0]
			more = self.neighbour[sq]
			#print more, 'asdf'
			if len(more) > 0:
				#print self.neighbour[sq]
				cell = random.choice(self.neighbour[sq])
				self.neighbour[sq].remove(cell)
				#print cell
				if self.colour[cell] == White:
					self.ClearWall(sq, cell)
					path.insert(0, cell)
					self.colour[cell] = Gray

			else:
				self.colour[sq] = Black
				del path[0]	

	def construct(self):
		'''Consturct maze of given height/width and size'''

		#print self.numcols, self.numrows
		self.colour = dict(((r, c), White)\
					for r in xrange(self.numrows) \
					for c in xrange(self.numcols))

		self.hasEastWall = dict(((r, c), False)\
						for r in xrange(self.numrows) \
						for c in xrange(self.numcols))
		
		#print self.hasEastWall							
		self.hasSouthWall = dict(((r, c), False)\
						for r in xrange(self.numrows) \
						for c in xrange(self.numcols))

		self.neighbour = dict(((r, c), [])\
						for r in xrange(self.numrows) \
						for c in xrange(self.numcols))

		for r in xrange(self.numrows):
			for c in xrange(self.numcols):
				n = self.numcols*r + c
				self.hasEastWall[r, c] = True
				self.hasSouthWall[r, c] = True

				if r != 0:
					self.neighbour[r, c].append((r - 1, c))

				if r != self.numrows - 1:
					self.neighbour[r, c].append((r + 1, c))

				if c != 0:
					self.neighbour[r, c].append((r, c - 1))

				if c != self.numcols - 1:
					self.neighbour[r, c].append((r, c + 1))
			
		sq = (0, self.numcols/2)
		self.dfsVisit_nr(sq)

		self.hasSouthWall[self.numrows - 1, self.numcols/2] = False						


if __name__ == '__main__':

	#a = map(int, raw_input().split())
	#m = Maze(a[0], a[1], a[2])
	m = Maze(400, 400, 50)
	m.view(1)		
