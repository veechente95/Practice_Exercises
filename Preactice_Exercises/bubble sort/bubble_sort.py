def bubble_sort(list):
    # -1 b/c we cant perform a comparison on last num in list because there is no number after it
    indexing_length = len(list) - 1
    sorted_list = False

    # perform as many iterations until sorted becomes True
    while not sorted_list:
        sorted_list = True

        # Once all values are sorted, if statement won't run, sorted_list will remain true and break out of while loop
        for i in range(0, indexing_length):
            if list[i] > list[i + 1]:   # if value to the left > right
                sorted_list = False     # sorted becomes False
                list[i], list[i + 1] = list[i + 1], list[i]   # swap numbers

    return list


print(bubble_sort([1, 9, 2, 8, 3, 7, 4, 5, 6]))