def getNthFib(n):
    lastTwo = [0,1]
    counter = 3
    while counter <= n:
        nthFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nthFib
        counter += 1
    if n > 1:
        return lastTwo[1]
    else:
        return lastTwo[0]

print(getNthFib(6))