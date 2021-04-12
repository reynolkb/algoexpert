# Best: O(n) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def insertionSort(array):
	for i in range(1, len(array)): # array starts at index 0 so you start at index 1 to insert
		j = i
		while j > 0 and array[j] < array[j-1]:
			swap(j, j - 1, array)
			j -= 1
	return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]

insertionSort([8, 5, 2, 9, 5, 6, 3])