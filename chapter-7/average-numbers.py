# average of even numbers

def average_of_even_numbers(array):
    # the mean is the sum of even numbers divided by the amount of even numbers
    sum = 0.0
    count_of_even_numbers = 0
    
    # iterate through each number in the array
    for i in array:
        number = i
        # if we encounter even number, the sum and count gets modified
        if number % 2 == 0:
            sum += number
            count_of_even_numbers += 1
    # return the mean average
    return sum / count_of_even_numbers 

print(average_of_even_numbers([1, 2, 3, 4, 4, 5, 6, 7, 8, 8]))   