# identify duplicate values in array
# Duplicate values should return true and non-duplicates should return false
import logging
# O(N)square algorith AKA very slow...
def hasDuplicateValue(array):
    steps = 0
    i = 0
    # iterate through each value of the array
    for i in range(len(array)):
        # j loops through array to check if values at positions i and j are the same
        j = 0
        for j in range(len(array)):
            steps += 1
            if i != j and array[i] == array[j]:
                return True
    
    return False


print(hasDuplicateValue([1, 2, 3, 4, 5, 6, 7, 8]))