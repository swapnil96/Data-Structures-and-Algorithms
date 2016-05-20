'''Link - www.spoj.com/problems/BST/'''
try:

	from functools import wraps

	def counter(func):

		@wraps(func)
		def tmp(*args, **kwargs):
			tmp.count += 1
			return func(*args, **kwargs)

		tmp.count = 0
		return tmp

	class BinaryNode:

		def __init__(self, value = None):
			'''Create binary node'''
		
			self.value = value
			self.right = None
			self.left = None

		@counter	
		def add(self, val):
			'''Adds new node to the tree containing this value'''
		
			if val <= self.value:
				if self.left:
					self.left.add(val)

				else:
					self.left = BinaryNode(val)	

			else:
				if self.right:
					self.right.add(val)

				else:
					self.right = BinaryNode(val)	

	class BinaryTree:

		def __init__(self):
			'''Create empty Binary tree'''
		
			self.root = None

		def add(self, value):
			'''Insert Value into proper location in Binary Tree'''
		
			if self.root is None:
				self.root = BinaryNode(value)

			else:	
				self.root.add(value)
				ans.append(self.root.add.count)

	ans = []
	ans.append(0)
	l = long(raw_input())
	que = []
	for i in xrange(l):
		a = long(raw_input())
		que.append(a)

	bt = BinaryTree()
	for i in xrange(l):
		bt.add(que[i])

	for i in xrange(l):
		print ans[i]	

except:
	sys.exit()
