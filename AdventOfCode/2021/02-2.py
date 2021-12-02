f = open("02.txt", "r")

x = 0
y = 0
aim = 0

for l in f.read().splitlines():
	word, num = l.split()
	if word == "forward":
		x += int(num)
		y += aim*int(num)
	elif word == "up":
		aim -= int(num)
	elif word == "down":
		aim += int(num)
	
print(x*y)
