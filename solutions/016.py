max = 1000
n = 2 ** max
S = str(n)

sum = 0
for c in range(len(S)):
	sum+=int(S[c:c+1])

print(sum) # 1366
