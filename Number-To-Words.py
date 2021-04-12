# ------------------------------------------------------- Number to words -------------------------------------------------------
num2words = {
    0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
    11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Ninteen', \
    20: 'Twenty', 30: 'Thirty', 40: 'Fourty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninty'
}

# def n2w (num):
#     if num < 0 or num > 99:
#         return ('number is not in range')
        
#     if num in num2words:
#         return(num2words[num])
#     else:
#         return(num2words[num // 10 * 10] + ' ' + num2words[num % 10])

# for num in range(-1, 101):
#     print(str(num) + ' ' + n2w(num))

# ------------------------------------------------------- Number to words 999 billion -------------------------------------------------------
MAXIMUM_INTEGER = 999999999999 # 999 billion

Multiples = (
    (1000000000, ' Billion '),
    (1000000, ' Million '),
    (1000, ' Thousand '),
    (100, ' Hundred '))

IntegerToWords = {
    1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
    10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Ninteen',
    20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}

def integerToWords(integer):
    '''
    This will build the return value 'words' by starting in the billions, and then working it's way down to 100.
    Note that integer will keep decreasing as words is built.
    '''
    # Initialize the return value
    words = ''

    # Deal with special values
    if integer == 0:
        return 'Zero'
    if MAXIMUM_INTEGER < integer:
        return 'Unknown'

    # negative number
    if integer < 0:
        words += 'Negative '
        integer *= -1

    # Determine the billions, millions, thousands, hundreds.
    for multiple, word in Multiples:
        if multiple <= integer:
            digit = integer // multiple # // is the floor operator
            integer -= digit * multiple # get rid of the multiple (e.g. 123 -> 23)
            words += integerToWords(digit) + word

    # Determine the remainder below 100
    if integer != 0:
        if integer in IntegerToWords:
            words += IntegerToWords[integer] # integer is directly in IntegerToWords
        else:
            words += IntegerToWords[integer // 10 * 10] + ' ' + IntegerToWords[integer % 10] # integer is 21, 32, 98, etc

    # Return words
    return words

print(integerToWords(-184))

# # Test loop for small numbers
# for i in range(-7, 108, 7):
#     print(str(i) + ': ' + integerToWords(i))

# # Test loop for bug numbers
# i = -1
# increment = 1
# while i <= MAXIMUM_INTEGER * 2:
#     print(str(i) + ': ' + integerToWords(i))
#     i += increment
#     increment *= 2