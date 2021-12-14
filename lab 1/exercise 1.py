from list_lib import *

# construct two doubly linked lists
l = double_link_list()
l.insert_tail(1)
l.insert_tail(2)
l.insert_tail(3)
l.insert_tail(4)
m = double_link_list()
m.insert_tail(5)
m.insert_tail(6)
m.insert_tail(7)
m.insert_tail(8)

# convert l as a single list
del l.head.previous
node_l = l.head.next
while node_l.next is not l.tail:
	del node_l.previous
	node_l = node_l.next
del l.tail
del node_l.previous
node_l.next = None

# convert m as a single list
node_m = start_m = m.head.next
del m.head
while node_m.next is not m.tail:
	del node_m.previous
	node_m = node_m.next
del m.tail
del node_m.previous
node_m.next = None

# concatenate the two link lists
node_l.next = start_m
node = l.head.next
while node is not None:
	print(node.data)
	node = node.next