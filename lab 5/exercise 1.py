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

left_tree = b_tree(7)
left_tree.left = b_tree(3)
left_tree.right = b_tree(4)

right_tree = tree
tree = b_tree(18)
tree.left = left_tree
tree.right = right_tree

# the worst running time is O(n)
tree.preorder()