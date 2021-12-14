from customized_map import *

class unsorted_map(my_map):
	def reset(self):
		headers = [linked_list() for _ in range(self.capacity * 2)]
		cap = self.capacity
		self.capacity = self.capacity * 2
		for i in range(cap):
			hash_list = self.headers[i]
			nodes = hash_list.get_list()
			for u in nodes:
				head = headers[u.key]
				head.append(u)
		self.headers = headers

	def put_only_absent(self, key, val):
		if key >= self.capacity:
			self.reset()
		hash_list = self.headers[key]
		if hash_list.empty():
			hash_list.append(node(key, val))
		else:
			return self.get(key)

	def get(self, key):
		if key < 0 or key >= self.capacity:
			return 'not find the key'
		hash_list = self.headers[key]
		tmp = hash_list.get_by_key(key)
		return tmp.val if tmp else 'no value'

	def delete(self, key):
		tmp = self.get(key)
		if tmp is None:
			return False
		hash_list = self.headers[key]
		hash_list.delete(tmp)
		return True

# test
my_sorted_map = unsorted_map(capacity=2)
my_sorted_map.put_only_absent(1, 1)
my_sorted_map.put_only_absent(3, 2)
my_sorted_map.put_only_absent(2, 3)
my_sorted_map.put_only_absent(5, 4)
my_sorted_map.put_only_absent(4, 5)
result = my_sorted_map.put_only_absent(6, 0)
print(result if result else '')
result = my_sorted_map.put_only_absent(2, 2)
print(result if result else '')
for item in my_sorted_map.headers:
	nodes = item.get_list()
	for n in nodes:
		print('key is %s, value is %s' % (str(n.key), str(n.val)))