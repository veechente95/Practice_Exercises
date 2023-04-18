# Quick Sort
# Divide and conquer
# 1) Chose pivot element (Usually last or random)
# 2) Store elements less than pivot in left subarray
# 3) Store elements greater than pivot in right subarray
# 4) Call quicksort recursively on left subarray
# 5) Call quicksort recursively on right subarray

def quick_sort(array):
    # for arrays that only have 1 or 0 numbers in sequence
    length = len(array)
    if length <= 1:
        return array
    else:
        # .pop() removes and return the number
        pivot = array.pop()

    # create 2 lists
    items_greater = []
    items_lower = []

    for num in array:
        if num > pivot:
            items_greater.append(num)
        else:
            items_lower.append(num)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print(quick_sort([11, 44, 33, 66, 77, 22, 55, 99, 88, 99]))