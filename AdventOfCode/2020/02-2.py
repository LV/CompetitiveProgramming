file = open('02.txt', 'r')
list = []

for line in file:
	list.append(line.strip())

def valid(lower, upper, char, string):
	return (char == string[lower-1]) ^ (char == string[upper-1])

def search():
	count = 0
	for i in range(len(list)):
		lower = list[i].split('-')[0]
		upper = (list[i].split('-')[1]).split(' ')[0]
		char = (list[i].split(' ')[1]).split(':')[0]
		string = list[i].split(' ')[2]
		if(valid(int(lower), int(upper), str(char), str(string))):
			count += 1
	
	print('total valid passwords: ' + str(count))

search()
