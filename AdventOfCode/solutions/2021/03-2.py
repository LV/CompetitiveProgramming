f = open("03.txt", "r")

lst = f.read().splitlines()

# Oxygen
oxylst = list(lst)
for i in range(12):
	newlist = []
	total = 0
	zeros = 0
	# count most common bit
	for j in range(len(oxylst)):
		total += 1
		if oxylst[j][i] == '0':
			zeros += 1
	if zeros > (total-zeros):
		fltr = 0
	else:
		fltr = 1
	# filter out values
	for j in range(len(oxylst)):
		if int(oxylst[j][i]) == fltr:
			newlist.append(oxylst[j])
	oxylst = newlist
	if(len(oxylst) == 1):
		break
oxygen = int(oxylst.pop(0), 2)


# C02
colst = list(lst)
for i in range(12):
	newlist = []
	total = 0
	zeros = 0
	# count most common bit
	for j in range(len(colst)):
		total += 1
		if colst[j][i] == '0':
			zeros += 1
	if zeros <= (total-zeros):
		fltr = 0
	else:
		fltr = 1
	# filter out values
	for j in range(len(colst)):
		if int(colst[j][i]) == fltr:
			newlist.append(colst[j])
	colst = newlist
	if(len(colst) == 1):
		break
co2 = int(colst.pop(0), 2)

print(co2*oxygen)
