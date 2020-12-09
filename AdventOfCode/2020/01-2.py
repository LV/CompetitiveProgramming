file = open('01.txt', 'r')
list = []

for line in file:
	list.append(int(line.strip()))

list.sort()

def search():
	for i in range(len(list)-2):
		for j in range(i+1, len(list)-1):
			for k in reversed(range(len(list))):
				if(list[i]+list[j]+list[k] == 2020):
					print('i: ' + str(list[i]) + ', j: ' + str(list[j]) + ', k: ' + str(list[k]))
					print('product: ' + str(list[i]*list[j]*list[k]))
					return
				elif(list[i]+list[j]+list[k] < 2020):
					break # all searches past this point are redundant
				else:
					continue

search()
