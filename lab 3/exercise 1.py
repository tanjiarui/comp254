def multiplication(m: int, n: int):
	assert m >= 0 and n >= 0
	if m == 0:
		return 0
	else:
		return multiplication(m - 1, n) + n

print(multiplication(5,5))