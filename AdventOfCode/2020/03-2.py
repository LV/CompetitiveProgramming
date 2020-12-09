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

def search(right, down):
	count = 0
	length = len(list)
	if(down == 2):
		length = int(length/2)

	for i in range(length):
		X = i*right
		Xcut = X % charPerLine
		
		if(isTree(list[i*down][Xcut])):
			count += 1

	return count

m11 = search(1,1)
m31 = search(3,1)
m51 = search(5,1)
m71 = search(7,1)
m12 = search(1,2)
	
print('1,1: ' + str(m11))
print('3,1: ' + str(m31))
print('5,1: ' + str(m51))
print('7,1: ' + str(m71))
print('1,2: ' + str(m12))
print('product = ' + str(m11 * m31 * m51 * m71 * m12))
