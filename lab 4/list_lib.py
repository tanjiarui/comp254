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
		while index:
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
		while index:
			if index.data == data:
				result.append(count)
			index = index.next
			count += 1
		return result

	def last(self):
		index = self.head.next
		while index.next:
			index = index.next
		return index

	def insert_head(self, data):
		x = node(data)
		x.next = self.head.next
		self.head.next = x

	def insert_tail(self, data):
		if self.empty():
			self.head.next = node(data)
		else:
			index = self.head.next
			while index.next:
				index = index.next
			index.next = node(data)

	def update(self, count, data):
		if count >= self.length():
			raise ValueError('invalid node')
		index = self.head.next
		for i in range(count):
			index = index.next
		index.data = data

	def remove(self, node):
		if self.empty():
			print('empty list')
			return
		pre, index = self.head, self.head.next
		while index is not node:
			pre = index
			index = index.next
		pre.next = index.next
		del index

	def delete(self):
		index = self.head.next
		self.head.next = None
		tmp = []
		while index:
			tmp.append(index)
			index = index.next
		del tmp

class linked_queue(link_list):
	def __iter__(self):
		cursor = self.head.next
		while cursor:
			yield cursor.data
			cursor = cursor.next

	def enqueue(self, data):
		self.insert_tail(data)

	def dequeue(self):
		value = self.head.next.data
		self.remove(self.head.next)
		return value

	def concatenate(self, queue):
		if not isinstance(queue, linked_queue):
			raise TypeError('queue must be a proper linked queue type')
		tail = self.last()
		tail.next = queue.head.next
		queue.head.next = None