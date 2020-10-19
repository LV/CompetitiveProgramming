number = 100

def factorial(n):
	if(n == 0 or n == 1):
		return 1
	else:
		product = 1
		for i in range(1,n+1):
			product *= i
	
	return product

fact = str(factorial(number))

sum = 0
for i in range(len(fact)):
	sum += int(fact[i:i+1])

print(sum) # 648
