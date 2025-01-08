import math

file = open('05.txt','r')
list = []

for line in file:
	list.append(line.strip())

example = 'BBFFBBFRLL'

def row(s):
	string = s[:-3]
	lower = 0
	upper = 127
	mid = upper/2
	
	for c in string:
		if(c == 'F'):
			upper = math.floor(mid)
			mid = lower + ((upper - lower) / 2)
		elif(c == 'B'):
			lower = math.ceil(mid)
			mid = upper - ((upper - lower) / 2)
	
	return int(mid)

def col(s):
	string = s[-3:]
	lower = 0
	upper = 7
	mid = upper/2

	for c in string:
		if(c == 'L'):
			upper = math.floor(mid)
			mid = lower + ((upper - lower) / 2)
		elif(c == 'R'):
			lower = math.ceil(mid)
			mid = upper - ((upper - lower) / 2)
	
	return int(mid)

def seatID(s):
	return (row(s)*8) + col(s)

id = []

def search():
	for l in list:
		id.append(seatID(l))

search()

id.sort()

print(id[-1])
