class node:
	def __init__(self, key, val, prev=None, succ=None):
		self.key = key
		self.val = val
		# previous
		self.prev = prev
		# successor
		self.succ = succ

class linked_list:
	def __init__(self):
		self.head = node(None, 'header')
		self.tail = node(None, 'tail')
		self.head.succ = self.tail
		self.tail.prev = self.head
		self.size = 0

	def append(self, node):
		prev = self.tail.prev
		node.prev = prev
		node.succ = prev.succ
		prev.succ = node
		node.succ.prev = node
		self.size += 1

	def empty(self):
		if self.size == 0:
			return True
		else:
			return False

	def delete(self, node):
		prev = node.prev
		succ = node.succ
		succ.prev, prev.succ = prev, succ
		self.size -= 1

	def get_list(self):
		ret = []
		cur = self.head.succ
		while cur != self.tail:
			ret.append(cur)
			cur = cur.succ
		return ret

	def get_by_key(self, key):
		cur = self.head.succ
		while cur != self.tail:
			if cur.key == key:
				return cur
			cur = cur.succ
		return None

class my_map():
	def __init__(self, capacity=16, load_factor=5):
		self.capacity = capacity
		self.load_factor = load_factor
		self.headers = [linked_list() for _ in range(capacity)]

	def reset(self):
		pass

	def put(self, key, val):
		pass

	def get(self, key):
		pass

	def delete(self, key):
		pass