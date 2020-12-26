def diagonal(n):
    if n % 2 == 0:
        return False
    elif n == 1:
        return 1
    else:
        iter_max = 2
        iter = 0
        curr = 0

        max = n ** 2
        sum = 1

        for i in range(2, max+1):
            iter += 1
            # print("i: " + str(i) + "   iter: " + str(iter) + "   i_max: " + str(iter_max))
            if iter == iter_max:
                sum += i
                # print("sum: " + str(sum))
                iter = 0
                curr += 1
                if curr == 4:
                    curr = 0
                    iter_max += 2
    return sum

print(diagonal(1001)) # 669171001
