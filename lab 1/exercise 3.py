from list_lib import *

list = circular_link_list()
list.insert_tail(1)
list.insert_tail(2)
list.insert_tail(3)
list.insert_tail(4)
diplicate = list.clone()
node = diplicate.head.next
while node is not diplicate.head:
	print(node.data)
	node = node.next