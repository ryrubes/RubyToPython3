# linear search on ordered array
def linear_search(array, search_value):
    for i in array:
        if i == search_value:
            return array[i]
        elif i > search_value:
            break

# searching for a value at a specified index
print(linear_search([1,2,3,4,8,10], 3))