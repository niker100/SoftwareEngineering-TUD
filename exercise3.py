# 3 3. Count how many six-digit numbers have equal sums of the first three and the last three digits.
def e3():
    count = 0
    for i in range(100000, 1000000):
        if sum([int(j) for j in str(i)[:3]]) == sum([int(j) for j in str(i)[3:]]):
            count += 1
    return count

print(e3())