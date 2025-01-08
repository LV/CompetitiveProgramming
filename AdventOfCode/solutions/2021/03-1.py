f = open("03.txt", "r")

total = 0
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for str in f.read().splitlines():
	total += 1
	for i in range(len(str)):
		if int(str[i]) == 1:
			count[i] += 1

def bin2dec(arr):
	num = 0
	digits = len(arr)
	for i in range(digits):
		num += arr[i] * (2**(digits-i-1))
	return num


gamma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(count)):
	if count[i] > total-count[i]:
		gamma[i] = 1


epsilon = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(len(gamma)):
	if gamma[i] == 1:
		epsilon[i] = 0

print(count)
print(gamma)
print(bin2dec(gamma))
print(epsilon)
print(bin2dec(epsilon))
print(bin2dec(gamma)*bin2dec(epsilon)) # result
