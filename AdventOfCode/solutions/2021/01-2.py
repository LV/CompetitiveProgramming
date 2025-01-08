f = open("01.txt", "r")

past = 0
curr = 0
sums = 0
tots = 0

dec = 0
inc = 0


for i in f.read().splitlines():
	tots = int(past) + int(curr) + int(i)

	if not(past == 0 or curr == 0):
		if tots > sums:
			inc += 1
		elif tots < sums:
			dec += 1
	
	sums = tots
	past = curr
	curr = i
	tots = 0

print(inc-1) # because the first number will always be greater than the stub
