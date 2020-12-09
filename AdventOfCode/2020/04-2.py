file = open('04.txt','r')
list = file.read().split('\n\n')
sectionedList = []

for i in range(len(list)):
	sectionedList.append(list[i].split())

def checkParts(p):
	for i in range(len(p)):
		curr = p[i].split(':')

		if(curr[0] == 'byr'):
			if(not(int(curr[1])>=1920 and int(curr[1])<=2002)):
				return False

		elif(curr[0] == 'iyr'):
			if(not(int(curr[1])>=2010 and int(curr[1])<=2020)):
				return False

		elif(curr[0] == 'eyr'):
			if(not(int(curr[1])>=2020 and int(curr[1])<=2030)):
				return False

		elif(curr[0] == 'hgt'):
			if(curr[1][-2:] == 'cm'):
				if(not(int(curr[1][:-2])>=150 and int(curr[1][:-2])<=193)):
					return False
			elif(curr[1][-2:] == 'in'):
				if(not(int(curr[1][:-2])>=59 and int(curr[1][:-2])<=76)):
					return False
			else:
				return False

		elif(curr[0] == 'hcl'):
			if(len(curr[1])==7):
				if(curr[1][0]=='#'):
					for c in curr[1][1:]:
						if(not((c>='0' and c<='9') or (c>='a' and c<='f'))):
							return False
				else:
					return False
			else:
				return False

		elif(curr[0] == 'ecl'):
			if(not(curr[1] == 'amb' or curr[1] == 'blu' or curr[1] == 'brn' or curr[1] == 'gry' or curr[1] == 'grn' or curr[1] == 'hzl' or curr[1] == 'oth')):
				return False

		elif(curr[0] == 'pid'):
			if(len(curr[1]) == 9):
				for c in curr[1]:
					if(not(c>='0' and c<='9')):
						return False
			else:
				return False
		
		elif(curr[0] == 'cid'):
			continue
		
		else:
			return False
	
	return True

def isValidPassport(p):
	if(len(p)<7):
		return False
	elif(len(p) == 7):
		for i in range(7):
			check = p[i][0:3]
			if(check == 'cid'):
				return False
		return checkParts(p)
	else:
		return checkParts(p)

def search():
	count = 0

	for i in range(len(sectionedList)):
		if(isValidPassport(sectionedList[i])):
			count += 1
	
	print('Valid passports: ' + str(count))

search()
