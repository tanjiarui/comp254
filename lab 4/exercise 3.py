from list_lib import *

queue1 = linked_queue()
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)
queue1.enqueue(4)
queue2 = linked_queue()
queue2.enqueue(5)
queue2.enqueue(6)
queue2.enqueue(7)
queue2.enqueue(8)
queue1.concatenate(queue2)
for item in queue1:
	print(item)