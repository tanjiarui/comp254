def upheap(arr, i):
	smallest = i
	left = 2 * i + 1
	right = 2 * i + 2
	if left < len(arr) and list(arr[left].keys())[0] < list(arr[smallest].keys())[0]:
		smallest = left
	if right < len(arr) and list(arr[right].keys())[0] < list(arr[smallest].keys())[0]:
		smallest = right
	if smallest != i:
		arr[i], arr[smallest] = arr[smallest], arr[i]
		upheap(arr, i//2)

arr = [{12:'a'}, {11:'b'}, {13:'c'}, {5:'d'}, {6:'e'}, {7:'f'}]
for i in range(len(arr)-1,-1,-1):
	upheap(arr, i)
print(arr)