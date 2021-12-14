def adjust_heap(data: [int], i, size):
	left = 2*i+1
	right = 2*i+2
	max = i
	if i < size/2: # have leaves in this case, size/2 means the last non-leaf
		if left < size and data[left] > data[max]:
			max = left
		if right < size and data[right] > data[max]:
			max = right
		if max != i:
			data[max], data[i] = data[i], data[max]

result =[]
array = [2,3,1,8,5,9,5,3,6,7,3,19,20,22,25]
size = len(array)
for i in range(10):
	for index in range(size//2)[::-1]:
		adjust_heap(array, index, size)
	result.append(array[0])
	array[0], array[size-1] = array[size-1], array[0]
	size -= 1
print(result)