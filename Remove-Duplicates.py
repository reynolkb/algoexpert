def removeDuplicates(arr):
    removed = set()
    for num in arr:
        removed.add(num)
    removed = list(removed)
    print(removed)

    # arr = list(set(arr))
    # print(arr)

removeDuplicates([1,1,1,1,2,2,2,3,3,3])