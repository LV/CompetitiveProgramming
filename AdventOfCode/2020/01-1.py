file = open('01.txt', 'r')
list = []

for line in file:
	list.append(line.strip())

def search():
	for i in range(len(list)-1):
		for j in range(i+1,len(list)):
			if(int(list[i]) + int(list[j]) == 2020):
				print('i: ' + str(list[i]) + ', j: ' + str(list[j]))
				print('product: ' + str((int(list[i]) * int(list[j]))))
				return

search()
