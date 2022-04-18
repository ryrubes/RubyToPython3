# calculate the median from an ordered array
import math
def median(array):
    middle = math.floor(len(array) / 2)

    # if array has even amount of numbers
    if (len(array) % 2 == 0):
        return (array[middle - 1] + array[middle]) / 2
    # if array has odd amount of numbers
    else:
        return array[middle]

print(median([1,2,3,4,5,6,7,8]))