from binary_tree import *

# build tree
right_tree = linked_binary_tree(6)
right_tree.left = linked_binary_tree(2)
right_tree.right = linked_binary_tree(4)

left_tree = linked_binary_tree(5)
left_tree.left = linked_binary_tree(1)
left_tree.right = linked_binary_tree(3)

tree = linked_binary_tree(11)
tree.left = left_tree
tree.right = right_tree

left_tree = linked_binary_tree(7)
left_tree.left = linked_binary_tree(3)
left_tree.right = linked_binary_tree(4)

right_tree = tree
tree = linked_binary_tree(18)
tree.left = left_tree
tree.right = right_tree
tree.print_tree(label=True)

# sum up its depths
length = []
level_order =[]

def left_child(node):
	return node.left if node.left is not None else None
def right_child(node):
	return node.right if node.right is not None else None

if tree.data is not None:
	level_order.append(tree)
height = tree.height()
if height >= 1:
	for node in level_order:
		if left_child(node):
			level_order.append(left_child(node))
		if right_child(node):
			level_order.append(right_child(node))
		length.append(node.height())
print('the path length is %d' % sum(length))