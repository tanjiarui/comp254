import uuid
from graphviz import Digraph
from random import sample

class linked_binary_tree(object):
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
		self.dot = Digraph(comment='Binary Tree')

	def preorder(self):
		if self.data is not None:
			print(self.data, end=' ')
		if self.left is not None:
			self.left.preorder()
		if self.right is not None:
			self.right.preorder()

	def inorder(self):
		if self.left is not None:
			self.left.inorder()
		if self.data is not None:
			print(self.data, end=' ')
		if self.right is not None:
			self.right.inorder()

	def postorder(self):
		if self.left is not None:
			self.left.postorder()
		if self.right is not None:
			self.right.postorder()
		if self.data is not None:
			print(self.data, end=' ')

	def height(self):
		if self.data is None:
			return 0
		elif self.left is None and self.right is None:
			return 0
		elif self.left is None and self.right is not None:
			return 1 + self.right.height()
		elif self.left is not None and self.right is None:
			return 1 + self.left.height()
		elif self.left is not None and self.right is not None:
			return 1 + max(self.left.height(), self.right.height())

	def print_tree(self, save_path='binary tree', label=False):
		# colors for labels of nodes
		colors = ['skyblue', 'tomato', 'orange', 'purple', 'green', 'yellow', 'pink', 'red']
		def print_node(node, node_tag):
			color = sample(colors, 1)[0]
			if node.left is not None:
				left_tag = str(uuid.uuid1())
				self.dot.node(left_tag, str(node.left.data), style='filled', color=color)
				label_string = 'L' if label else ''
				self.dot.edge(node_tag, left_tag, label=label_string)
				print_node(node.left, left_tag)

			if node.right is not None:
				right_tag = str(uuid.uuid1())
				self.dot.node(right_tag, str(node.right.data), style='filled', color=color)
				label_string = 'R' if label else ''
				self.dot.edge(node_tag, right_tag, label=label_string)
				print_node(node.right, right_tag)

		if self.data is not None:
			root_tag = str(uuid.uuid1())
			self.dot.node(root_tag, str(self.data), style='filled', color=sample(colors, 1)[0])
			print_node(self, root_tag)

		self.dot.render(save_path)