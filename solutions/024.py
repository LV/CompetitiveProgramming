def swapChar(s, i, j):	# a < b
	s = list(s)
	s[i], s[j] = s[j], s[i]
	return ''.join(s)

def concatenate(s, lst):
	for i in range(len(lst)):
		lst[i] = s + lst[i]
	return lst

def permutate(s):
	lst = []
	if len(s) == 1:
		lst.append(s)
	else:
		for i in range(len(s)):
			new_str = swapChar(s, 0, i)
			new_list = permutate(new_str[1:])
			new_list = concatenate(new_str[0:1], new_list)
			for j in new_list:
				lst.append(j)
	lst.sort()
	return lst

print(permutate('0123456789')[999999]) # 2783915460
