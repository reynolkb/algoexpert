# O(2^n) time | O(n) space
# def getNthFib(n):
#     if n == 2:
#         return 1
#     elif n == 1:
#         return 0
#     else:
#         return getNthFib(n-1) + getNthFib(n-2)

# O(n) time | O(1) space
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

print(getNthFib(4))