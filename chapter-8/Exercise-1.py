# returns the intersection of two arrays
# the third array stores any values that array1 and array2 both share
def insert_two_arrays(array1, array2):
    third_array  = []

    for i in array1:
        for j in array2:
            if i == j:
                third_array.append(i)
            if i != j:
                continue
    print(third_array)        

insert_two_arrays([1,2,3,4,5], [1,3,5])

