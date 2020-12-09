file = open('04.txt','r')
list = file.read().split('\n\n')
sectionedList = []

for i in range(len(list)):
	sectionedList.append(list[i].split())

def isValidPassport(p):
	if(len(p)<7):
		return False
	elif(len(p) == 8):
		return True
	else:
		for i in range(7):
			check = p[i][0:3]
			if(check == 'cid'):
				return False
		return True

def search():
	count = 0

	for i in range(len(sectionedList)):
		if(isValidPassport(sectionedList[i])):
			count += 1
	
	print('Valid passports: ' + str(count))

search()
