# Big O notation

# sum up all the numbers in a given array
# Exercise 2:
def arraysum(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum

print((arraysum([1,2,3,4,5,6,7,8,9,10])))