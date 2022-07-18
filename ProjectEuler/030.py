power = 5

def digit_sum(num):
	sum = 0
	str_num = str(num)
	for c in str_num:
		sum += int(c) ** power
	return sum

sum_nums = 0
for i in range(2,999999):
	if i == digit_sum(i):
		sum_nums += i

print(sum_nums) # 443839
