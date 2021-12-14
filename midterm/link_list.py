class node:
	def __init__(self, data, pointer=None):
		self.data = data
		self.next = pointer

class link_list:
	def __init__(self):
		self.head = node(None, None)

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
		x = node(data)
		x.next = self.head.next
		self.head.next = x

	def insert_tail(self, data):
		if self.empty():
			self.head.next = node(data)
		else:
			index = self.head.next
			while index.next is not None:
				index = index.next
			index.next = node(data)

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