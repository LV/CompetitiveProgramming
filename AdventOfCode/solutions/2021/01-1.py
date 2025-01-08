f = open("01.txt", "r")

past = 150 # using this as base case since first number on file is 150 (prevent dec or inc count from chaning)

dec = 0
inc = 0

for i in f.read().splitlines():
	if i > past:
		inc += 1
	elif i < past:
		dec += 1
	
	past = i

print(inc)
