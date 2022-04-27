# multiplies two numbers and appends to output to the end of array
# example: 1*2 = 2... so 2 will be appended to the array
def twoNumberProducts(array):
    prodcuts = []

    # outer array
    for i in range(len(array)):
        # inner array
        for j in range(len(array)):
            # append solutions to products array
                    prodcuts.append(array[i] * array[j])

    return prodcuts

print(twoNumberProducts([1,2,3,4,5,6]))