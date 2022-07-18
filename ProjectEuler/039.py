from math import sqrt

from numpy import isin


def hypothenus(a, b):
	ans = sqrt((a*a) + (b*b))
	if ans == int(ans):
		return int(ans)
	else:
		return False

def counter(perimiter):
	count = 0
	for i in range(1, int(perimiter/2)+1):
		for j in range(i, int(perimiter/2)+1):
			hyp = perimiter - i - j
			if(hyp<=i or hyp<=j):
				continue

			ans = hypothenus(i, j)
			if ans == hyp:
				count += 1
	
	return count

max_num = -1
max_amount = -1
for x in range(2, 1000):
	cnt = counter(x)
	if cnt > max_amount:
		max_amount = cnt
		max_num = x

print(max_num) # 840
