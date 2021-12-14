def func(a, b=5, c=10, **others):
	print('a is', a, 'and b is', b, 'and c is', c)
	print('other arguments: %s' % others)

func(3, 7)
func(25, c=24)
func(c=50, a=100)
func(2, d=20, e=30, f=40)