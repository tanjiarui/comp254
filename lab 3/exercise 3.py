import os

def find_file(path: str, filename: str):
	if os.path.isdir(path):
		list = os.listdir(path)
		list.sort()
		for item in list:
			path = os.path.join(path, item)
			path = find_file(path, filename)
	else:
		if os.path.split(path)[1] == filename:
			print(path)
	return os.path.split(path)[0]

find_file('/home/ubuntu/文档/data structure','exercise 3.py')