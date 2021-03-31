# O(n) time | O(n) space
# def twoNumberSum(array, targetSum):
#     nums = {}
#     for num in array:
#         potentialMatch = targetSum - num
#         if potentialMatch in nums:
#             return num, potentialMatch
#         else:
#             nums[num] = True
#     return []

def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
        elif currentSum == targetSum:
            return array[left], array[right]
    return []
