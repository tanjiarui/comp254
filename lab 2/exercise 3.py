import numpy as np, time

def unique1(array: []):
	n = len(array)
	for i in range(n - 1):
		for j in range(i + 1, n):
			if array[i] == array[j]: return False
	return True

def unique2(array: []):
	n = len(array)
	array.sort()
	for i in range(n - 1):
		if array[i] == array[i + 1]: return False
	return True

def search_largest_size(function: str, min_size: int, max_size: int, time_limit=60):
	size = (min_size + max_size) // 2
	array = list(np.random.randint(101, size=size))
	if size < max_size and min_size != max_size:
		if function == 'unique1':
			start = time.time()
			unique1(array)
			end = time.time()
			elapse = end - start
			print('array size: ' + str(size) + '\telapse time: ' + str(elapse))
		elif function == 'unique2':
			start = time.time()
			unique2(array)
			end = time.time()
			elapse = end - start
			print('array size: ' + str(size) + '\telapse time: ' + str(elapse))
		else:
			print('invalid function name')
			return
		if abs(elapse - time_limit) < .001:
			del array
			return size
		elif elapse < time_limit:
			del array
			return search_largest_size(function, size + 1, max_size, time_limit)
		elif elapse > time_limit:
			del array
			return search_largest_size(function, min_size, size - 1, time_limit)
	return size

# time limit can't be set too large because it is time and memory consuming.
size1 = search_largest_size('unique1', 0, 100000000, 1)
size2 = search_largest_size('unique2', 0, 10000000000, 1)