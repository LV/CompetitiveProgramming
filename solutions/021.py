def list_divisors(n):
	lst = []
	lst.append(1)
	for i in range(2, (int((n ** 0.5)+1))):
		if n % i == 0:
			lst.append(i)
			divided = int(n/i)
			if(i != divided):
				lst.append(divided)
	lst.sort()
	return lst

def list_sum(lst):
	sum = 0
	for e in lst:
		sum += e
	return sum

def isAmicable(n):
	b_sum = list_sum(list_divisors(n))
	if b_sum == n:	# Cases of 6 and 28 return b_sum as their own numbers which is a problem
		return False
	else:
		return list_sum(list_divisors(b_sum)) == n

sum = 0
for i in range(10000):
	if isAmicable(i):
		sum += i

print(sum) # 31626
