def next_collatz(n):
	if(n % 2 == 0):
		return n/2
	else:
		return (3*n) + 1

def count_collatz(n):
	count = 1

	finished = False

	while(not finished):
		count += 1
		n = next_collatz(n)
		if(n == 1):
			finished = True
	
	return count


maximum = 0
number = 0
for i in range(600000, 1000001): # Making an educated guess that the answer will lie in this range
	total = count_collatz(i)
	if(total > maximum):
		maximum = total
		number = i

print(number) # 837799
