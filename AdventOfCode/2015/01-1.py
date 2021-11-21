f = open("01.txt", "r")
i = 0

for char in f.read():
    if char == "(":
        i += 1
    elif char == ")":
        i -= 1

print(i)
