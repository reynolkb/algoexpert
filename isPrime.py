def isPrime(num):
    '''
    Given a number return if it is prime. Number is not negative and 2 is the first prime number
    '''
    if type(num) != int:
        return('please enter an integer')

    # edge case to determine if the number is 0
    if num == 0:
        return('The number is 0 and is neither prime nor composite')
    
    # edge case for 1
    if num == 1:
        return('composite')

    # edge case to determine if the number is 2
    if num == 2:
        return('prime')

    # if the number is not 0, 1, or 2, start at 2 and loop through each number and see if the remainder is 0
    # if the number is evenly divisible by any number in range of 2 - (num - 1) then return composite
    # if you've gone through the loop and have not returned composite, return prime
    for i in range(2, num):
        if num % i == 0:
            return 'composite'
    return 'prime'

print(isPrime(3))