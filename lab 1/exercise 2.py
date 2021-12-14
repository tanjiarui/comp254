from list_lib import *

def swap_node(node1_pre:node2, node2_pre:node2):
	node_a, node_b = node1_pre.next, node2_pre.next
	if node_a is None or node_b is None:
		print('out of range')
		exit()
	node1_pre.next, node2_pre.next = node_b, node_a
	node_a.next, node_b.next = node_b.next, node_a.next

list = link_list()
list.insert_tail(1)
list.insert_tail(2)
list.insert_tail(3)
list.insert_tail(4)
# mark the previous nodes that needed to swap
node1_pre = list.head.next
node2_pre = list.head.next.next.next
swap_node(node1_pre,node2_pre)
node = list.head.next
while node is not None:
	print(node.data)
	node = node.next
