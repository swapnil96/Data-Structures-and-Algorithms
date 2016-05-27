'''Implementation of KDtree'''

maxValue = 2147483647
minValue = -2147483647

Vertical = 1
Horizontal = 0

X_ = 0
Y_ = 1

class Region:

	def __init__(self, xmin, ymin, xmax, ymax):
		'''Creates region from (xmin, ymin) to (xmax, ymax)'''

		self.x_min = xmin
		self.y_min = ymin
		self.x_max = xmax
		self.y_max = ymax

	def copy(self):
		'''Return copy of region'''

		return Region(self.x_min, self.y_min, self.x_max, self.y_max)

#Default maximum region
maxRegion = Region(minValue, minValue, maxValue, maxValue)
'''To specify a region pass - r = Region(0, 0, 100, 100)'''

class KDnode:

	def __init__(self, pt, orient, region = maxRegion):
		'''Create enpty KDnode'''

		self.point = pt
		self.orient = orient
		self.region = region
		self.above = None
		self.below = None

	def createChild(self, pt, below):
		'''Create child node (either above or below) given node with point'''

		r = self.region.copy()
		if self.orient == Vertical:
			if below:
				r.x_max = self.point[X_]

			else:
				r.x_min = self.point[X_]

		else:
			if below:
				r.y_max = self.point[Y_]

			else:
				r.y_min = self.point[Y_]

		return KDnode(pt, 1 - self.orient, r)
							
	def isBelow(self, pt):
		'''Is point below current node'''

		if self.orient == Vertical:
			return pt[X_] < self.point[X_]

		return pt[Y_] < self.point[Y_]
									
	def add(self, pt):
		'''Add point to the KDnode tree rooted at this node'''

		if self.point == pt:
			return

		if self.isBelow(pt):
			if self.below:
				self.below.add(pt)

			else:
				self.below = self.createChild(pt, True)

		else:
			if self.above:
				self.above.add(pt)

			else:
				self.above = self.createChild(pt, False)

class KDtree:

	def __init__(self):
		'''Create empty KDtree'''

		self.root = None

	def add(self, pt):
		'''Add point to KDtree'''

		if self.root:
			self.root.add(pt)

		else:
			self.root = KDnode(pt, Vertical)	

if __name__ == '__main__':
	kd = KDtree()
	p0 = [10, 10]
	kd.add(p0)
	print kd.root.point, kd.root.orient, kd.root.region, kd.root.region.x_min			
	p1= [20, 20]
	kd.add(p1)
	print kd.root.above.point