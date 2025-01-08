f = open("02.txt", "r")

x = 0
y = 0

for l in f.read().splitlines():
	word, num = l.split()
	if word == "forward":
		x += int(num)
	elif word == "up":
		y -= int(num)
	elif word == "down":
		y += int(num)
	
print(x*y)
