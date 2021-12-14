from link_list import *

new_head = node(None)
def reverse(pre: node):
	if pre.next is None:
		new_head.next = pre
	else:
		cur = reverse(pre.next)
		cur.next = pre
		if pre.data is None:
			cur.next = None
	return pre

l = link_list()
l.insert_tail(1)
l.insert_tail(2)
l.insert_tail(3)
l.insert_tail(4)
reverse(l.head)
node = new_head.next
while node is not None:
	print(node.data)
	node = node.next