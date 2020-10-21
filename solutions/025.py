prv = 1
cur = 1
nxt = 0
counter = 2

digits = 1000

while(cur < (10 ** (digits - 1))):
	nxt = prv + cur
	prv = cur
	cur = nxt
	counter += 1

print(counter) # 4782
