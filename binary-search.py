def binary_search(array, search_value):
    # lower bound is the first value in array
    # upper bound is the last value in array
    lower_bound = 0
    upper_bound = len(array) - 1

# get midpoint or meduian then
# set mid value as value to return value instead of index position
    while lower_bound <= upper_bound:
        midpoint = (lower_bound + upper_bound) // 2
        midpoint_value = array[midpoint]
        # inspect midpoint value
        # then return position
        if midpoint_value == search_value:
            return midpoint

        elif search_value < midpoint_value:
            upper_bound = midpoint - 1

        else:
            lower_bound = midpoint + 1
    return None
array = [5, 10, 15, 100, 500]
search_value = 15

print(binary_search(array, search_value))
    