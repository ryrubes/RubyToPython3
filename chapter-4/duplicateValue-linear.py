# much more efficient linear solution and doesnt rely on nested loops

# O(N) algorithm
def hasDuplicateValue(array):
    existingNumbers = []

    # for each element in array
    for n in array:
        # store absolute value of each number incase its negative
        m = abs(n)

        # append any re-visited numbers to existingNumbers array
        if array[m-1] < 0:
            existingNumbers.append(m)
            return True

        # if theres a negative value multiply it by -1 to get positive
        else:
            array[m-1] *= -1

    return False

print(hasDuplicateValue([1,2,3,3,5,6,7]))