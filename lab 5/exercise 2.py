from binary_tree import *

right_tree = b_tree(6)
right_tree.left = b_tree(2)
right_tree.right = b_tree(4)

left_tree = b_tree(5)
left_tree.left = b_tree(1)
left_tree.right = b_tree(3)

tree = b_tree(11)
tree.left = left_tree
tree.right = right_tree

def print_height(node):
	if node.data:
		print(node.height())
	if node.left:
		print_height(node.left)
	if node.right:
		print_height(node.right)

print_height(tree)
tree.print_tree(label=True)