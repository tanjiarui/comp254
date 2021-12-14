from customized_map import *

class hash_map(my_map):
	def get_hash_key(self, key):
		return hash(key) & (self.capacity - 1)

	def reset(self):
		headers = [linked_list() for _ in range(self.capacity * 2)]
		cap = self.capacity
		self.capacity *= 2
		for i in range(cap):
			hash_list = self.headers[i]
			nodes = hash_list.get_list()
			for u in nodes:
				hash_key = self.get_hash_key(u.key)
				head = headers[hash_key]
				if head.empty():
					head.append(u)
				else:
					hash_key += 1
					while hash_key < self.capacity:
						new_head = headers[hash_key]
						if new_head.empty():
							new_head.append(u)
							break
						else:
							hash_key += 1
					if hash_key == self.capacity:
						head.append(u)
		self.headers = headers

	def put(self, key, val):
		hash_key = self.get_hash_key(key)
		hash_list = self.headers[hash_key]
		if hash_list.size >= self.load_factor * self.capacity:
			self.reset()
			hash_key = self.get_hash_key(key)
			hash_list = self.headers[hash_key]
		if hash_list.empty():
			hash_list.append(node(key, val))
		else:
			hash_key += 1
			while hash_key < self.capacity:
				nuw_hash_list = self.headers[hash_key]
				if nuw_hash_list.empty():
					nuw_hash_list.append(node(key, val))
					break
				else:
					hash_key += 1
			if hash_key == self.capacity:
				hash_list.append(node(key, val))

	def get(self, key):
		hash_key = self.get_hash_key(key)
		hash_list = self.headers[hash_key]
		tmp = hash_list.get_by_key(key)
		if tmp:
			return [hash_list, tmp]
		else:
			hash_key += 1
			while hash_key < self.capacity:
				hash_list = self.headers[hash_key]
				tmp = hash_list.get_by_key(key)
				if tmp:
					return [hash_list, tmp]
				else:
					hash_key += 1
			return None

	def delete(self, key):
		hash_list, tmp = self.get(key)
		if tmp is None:
			return False
		hash_list.delete(tmp)
		return True


# hash map is implemented by a linked list. using linear probing to avoid collision
my_hash_map = hash_map(capacity=2, load_factor=2)
my_hash_map.put(1, 1)
my_hash_map.put(1, 2)
my_hash_map.put(1, 3)
my_hash_map.put(1, 4)
my_hash_map.put(1, 5)
for item in my_hash_map.headers:
	nodes = item.get_list()
	for n in nodes:
		print('key is %s, value is %s' % (str(n.key), str(n.val)))