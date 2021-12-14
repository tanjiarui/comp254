def palindrome(string: str):
	if not string.strip():
		return False
	if len(string) == 1:
		return True
	if len(string) == 2:
		if string[0] == string[-1]:
			return True
		else:
			return False
	if string[0] == string[-1]:
		return palindrome(string[1:-1])
	else:
		return False

print(palindrome(''))
print(palindrome('racecar'))
print(palindrome('racer'))
print(palindrome('gohangasalamiimalasagnahog'))