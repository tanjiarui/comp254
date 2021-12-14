import numpy as np, matplotlib.pyplot as plt, time

def prefix_average1(array:[]):
	n = len(array)
	avg = []
	for i in range(n):
		total = 0
		for j in range(i+1):
			total += array[j]
		avg.append(total / (i + 1))
	return avg

def prefix_average2(array:[]):
	n = len(array)
	avg = []
	total = 0
	for i in range(n):
		total += array[i]
		avg.append(total / (i + 1))
	return avg

def evaluation(function:str,epoch:int,initial=10):
	elapse = []
	for test in range(1,epoch+1):
		arr_size = 100*test*initial
		array = list(np.random.randint(101, size=arr_size))
		if function == 'prefix_average1':
			start = time.time()
			prefix_average1(array)
			end = time.time()
			elapse.append(end-start)
			print('array size: ' + str(arr_size) + '\telapse time: ' + str(end - start))
		elif function == 'prefix_average2':
			start = time.time()
			prefix_average2(array)
			end = time.time()
			elapse.append(end-start)
			print('array size: ' + str(arr_size) + '\telapse time: ' + str(end - start))
		else:
			print('invalid function name')
			exit()
	return elapse

elapse1 = evaluation('prefix_average1',10)
elapse2 = evaluation('prefix_average2',10)

epoch = range(1,11)
line1 = plt.plot(epoch, elapse1, color='red', linewidth=2.0, linestyle='--', label='prefix_average1')
line2 = plt.plot(epoch, elapse2, color='blue', linewidth=3.0, linestyle='-.', label='prefix_average2')
plt.title('analysis of prefix_average')
plt.xlabel('epoch')
plt.ylabel('runtime')
plt.legend()
plt.show()