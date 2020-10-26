# A much nicer solution to number 5

def is_prime(n):
	if n == 2:
		return True
	elif n == 3:
		return True
	else:
		limit = int(n ** 0.5)
		for i in range(2, limit+1):
			if n % i == 0:
				return False
		return True

n = 100
l = []

for i in range(2, n+1):
	if is_prime(i):
		num = i
		while(num<=n):
			l.append(i)
			num *= i

total_product = 1
for j in l:
	total_product *= j

print(total_product)
