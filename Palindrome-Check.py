# def isPalindrome(string):
#     string = string.lower().replace(' ', '')

#     reverse = string[::-1]
#     if(string == reverse):
#         return True
#     return False

# O(n) time | O(n) space
# def isPalindrome(string):
#     reversedChars = []
# # the length of the string is 7. range of 7 is 0-6 excluding final number. 
# # reversed looks at index 6 first which is the last letter in the list
#     for i in reversed(range(len(string))):
#     	reversedChars.append(string[i])
#     return string == "".join(reversedChars)

# O(n) time | O(1) space
def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
    	if string[leftIdx] != string[rightIdx]:
    		return False
    	leftIdx += 1
    	rightIdx -= 1
    return True

print(isPalindrome('abcdcba'))