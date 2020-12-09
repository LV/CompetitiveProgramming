file = open('03.txt','r')
list = []

for line in file:
	list.append(line.strip())

charPerLine = 31

def isTree(c):
	if(c == '#'):
		return True
	else:
		return False

def search(right):
	count = 0

	for i in range(len(list)):
		X = i*right
		Xcut = X % charPerLine
		
		if(isTree(list[i][Xcut])):
			count += 1

	print('Trees encountered: ' + str(count))
	
search(3)
