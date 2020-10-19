dimension = 20

def factorial(i):
	if(i == 0 or i == 1):
		return 1
	else:
		product = 1
		for j in range(1, i+1):
			product *= j
		return product

n = factorial(dimension * 2)
r = factorial(dimension)

print(int(n/(r*r))) # 137846528820

""" Heres my initial version of the program:

dimension = 2

def visit(x, y):
    count = 0
    if(x == dimension and y == dimension):
        return 1
    elif(x == dimension):
        count += visit(x, y+1)
        return count
    elif(y == dimension):
        count += visit(x+1, y)
        return count
    else:
        count += visit(x+1, y)
        count += visit(x, y+1)
        return count

print(visit(0, 0))

And it would work. But upon going into dimension 20, the program was useless. After some hairpulling, I discovered that the paths could be written in binary format (1 meaning right, 0 meaning down) that I came to discover than an equal number of 0s and 1s are necessary and could actually be arranged in any format so long as the same number of 0s and 1s existed.

It led to the discovery that the program I wrote was just a very bad nCr calculator and that this problem was simple a nCr problem and led to the development of a simple nCr program.
"""
		
