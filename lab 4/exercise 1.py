from positional_list import *

l = positional_list()
p = l.add_first('a')
print(l.index(p))
p = l.add_after(p, 'b')
print(l.index(p))
p = l.add_after(p, 'c')
print(l.index(p))
p = l.add_after(p, 'd')
print(l.index(p))