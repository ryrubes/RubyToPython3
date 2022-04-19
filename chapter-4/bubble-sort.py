def bubble_sort(list):
    unsorted_until_index = len(list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            # if element in list is greater than the element to the right
            if list[i] > list[i+1]:
                # swap the order of the two and if thats needed, change sorted to False
                list[i], list[i+1] = list[i+1], list[i]
                sorted = False
        unsorted_until_index -= 1
    return list

print(bubble_sort([100, 50, 23, 81, 55]))

# O(N squared) which isn't very efficient algorithm