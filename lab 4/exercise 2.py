def transfer(s: [], t: []):
	while s:
		t.append(s.pop())

def test():
	s, t = [], []
	s.append('peony')
	s.append('cherry blossoms')
	s.append('winter sweet')
	s.append('orchid')
	s.append('poppy')
	return s, t

stack_a, stack_b = test()
print(stack_a)
transfer(stack_a, stack_b)
print(stack_b)