# Quick Sort
# Divide and conquer
# 1) Chose pivot element (Usually last or random)
# 2) Store elements less than pivot in left subarray
# 3) Store elements greater than pivot in right subarray
# 4) Call quicksort recursively on left subarray
# 5) Call quicksort recursively on right subarray

def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        # quicksort all elements less than pivot element to the left
        quicksort(arr, left, partition_pos - 1)
        # quicksort all elements greater than pivot to the right
        quicksort(arr, partition_pos + 1, right)


# func returns index of pivot element after the first step of quicksort
def partition(arr, left, right):
    i = left
    j = right
    pivot_element = arr[right]

    # i moves to the right and j moves to the left until i and j cross
    while i < j:
        # while i is not at the end of array
        while i < right and arr[i] < pivot_element:
            i += 1
        # while j is not at the end of array
        while j > left and arr[j] >= pivot_element:
            j -= 1

        # check if i and j elements have crossed. Also check if they didn't cross and swap numbers
        if i < j:
            # swap element at index i with index j
            arr[i], arr[j] = arr[j], arr[i]

    # if array at index i is greater than pivot, we need to do another swap and swap those elements
    if arr[i] > pivot_element:
        arr[i], arr[right] = arr[right], arr[i]

    # quicksort func needs this i to determine where to split the array to call quick sort recursively
    return i


# 44 is the pivot number (Usually last number or random)
arr = [22, 11, 88, 66, 55, 77, 33, 44]
quicksort(arr, 0, len(arr) - 1)
print(arr)