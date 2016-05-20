'''Binary Search Tree implementation'''

class BinaryNode:

	def __init__(self, value = None):
		'''Create binary node'''
		
		self.value = value
		self.right = None
		self.left = None

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

	def delete(self):
		'''Remove value of self from Binary Tree. Works in conjuction
		woth remove method in BinaryTree'''			
		
		if self.right == self.left == None:
			return None

		if self.left == None:
			return self.right

		if self.right == None:
			return self.left		

		child = self.left
		grandchild = child.right
		if grandchild:
			while grandchild.right:
				child = grandchild
				grandchild = child.right

			self.value = grandchild.value
			child.right = grandchild.left

		else:
			self.left = child.left
			self.value = child.value

		return self


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

	def contains(self, target):
		'''Check whether BST contains target value'''
		
		node = self.root
		while node:
			
			if target == node.value:
				return True

			elif target < node.value:
				node = node.left

			else:		
				node = node.right

		return False

	def remove(self, value):
		'''Remove value from tree'''

		if self.root:
			self.root = self.removeFromParent(self.root, value)

		
	def removeFromParent(self, parent, value):
		'''remove value from tree rooted at parent'''

		if parent is None:
			return None

		if value == parent.value:
			return parent.delete()

		elif value < parent.value:
			parent.left = self.removeFromParent(parent.left, value)

		else:
			parent.right = self.removeFromParent(parent.right, value)

		return parent
					
if __name__  ==  "__main__":
	bt = BinaryTree()
	bt.add(5)
	bt.add(1)
	bt.add(10)
	print bt.contains(5)
	bt.remove(5)
	print bt.contains(1)

