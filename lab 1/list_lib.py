class node1:
	def __init__(self, data, p=None, q=None):
		self.data = data
		self.previous = p
		self.next = q

class double_link_list:
	def __init__(self):
		self.head = node1(None, None, None)
		self.tail = node1(None, None, None)
		self.head.next, self.tail.previous = self.tail, self.head

	def length(self):
		count = 0
		index = self.head.next
		while index is not self.tail:
			count += 1
			index = index.next
		return count

	def empty(self):
			return self.head.next is self.tail

	def insert_head(self, data):
		x = node1(data)
		x.next, self.head.next.previous = self.head.next, x
		self.head.next, x.previous = x, self.head

	def insert_tail(self, data):
		x = node1(data)
		x.previous, self.tail.previous.next = self.tail.previous, x
		x.next, self.tail.previous = self.tail, x

class node2:
	def __init__(self, data, pointer=None):
		self.data = data
		self.next = pointer

class link_list:
	def __init__(self):
		self.head = node2(None, None)

	def length(self):
		count = 0
		index = self.head.next
		while index is not None:
			count += 1
			index = index.next
		return count

	def empty(self):
			return self.head.next is None

	def search(self, data):
		if self.empty():
			print('empty list')
			return
		result = []
		index = self.head.next
		count = 0
		while index is not None:
			if index.data == data:
				result.append(count)
			index = index.next
			count += 1
		return result

	def insert_head(self, data):
		x = node2(data)
		x.next = self.head.next
		self.head.next = x

	def insert_tail(self, data):
		if self.empty():
			self.head.next = node2(data)
		else:
			index = self.head.next
			while index.next is not None:
				index = index.next
			index.next = node2(data)

	def update(self, count, data):
		if count >= self.length():
			raise ValueError('invalid node')
		index = self.head.next
		for i in range(count):
			index = index.next
		index.data = data

	def remove(self, data):
		if self.empty():
			print('empty list')
			return
		pre = self.head
		index = self.head.next
		while index is not None:
			if index.data == data:
				pre.next = index.next
				del index
				index = pre.next
			pre = index
			if pre is not None:
				index = index.next

	def delete(self):
		index = self.head.next
		self.head.next=None
		tmp=[]
		while index is not None:
			tmp.append(index)
			index = index.next
		del tmp

class circular_link_list:
	def __init__(self):
		self.head = node2(None, None)
	
	def length(self):
		count = 0
		index = self.head.next
		while index is not self.head:
			count += 1
			index = index.next
		return count

	def empty(self):
			return self.head.next is None

	def insert_head(self, data):
		x = node2(data)
		x.next = self.head.next
		self.head.next = x

	def insert_tail(self, data):
		if self.empty():
			self.head.next = node2(data)
			self.head.next.next = self.head
		else:
			index = self.head.next
			while index.next is not self.head:
				index = index.next
			index.next = node2(data)
			index.next.next = self.head

	def clone(self):
		duplicate = circular_link_list()
		if self.empty():
			return duplicate
		node = self.head.next
		while node is not self.head:
			duplicate.insert_tail(node.data)
			node = node.next
		return duplicate