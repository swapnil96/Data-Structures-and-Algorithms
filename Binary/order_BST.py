'''Given an ordered list, Create a balanced BST'''

from BST import BinaryTree

def addRange(bt, ordered, low, high):
	'''Add range to bt in way that bt remains balanced'''

	if low <= high:
		
		mid = (low + high)/2
		bt.add(ordered[mid])
		addRange(bt, ordered, low, mid - 1)
		addRange(bt, ordered, mid + 1, high)


def balancedTree(ordered):
	'''Create balanced Binary Tree from Ordered Collection'''

	bt = BinaryTree()

	addRange(bt, ordered, 0, len(ordered) - 1)

	return bt


x = range(10)
bt = balancedTree(x)
print bt.root.value
print bt.root.left.value
print bt.root.right.value
