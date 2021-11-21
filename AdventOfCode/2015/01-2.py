f = open("01.txt", "r")
i = 0
j = 0

for char in f.read():
    j += 1
    if char == "(":
        i += 1
    elif char == ")":
        i -= 1
    if i < 0:
        print(j)
        break

print(i)
