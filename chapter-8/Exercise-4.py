# function that returns the first non-duplicated character in a string
non_duplicates = []
def non_duplicate(string):
    for char in string:
        if string.count(char) == 1:
            x = non_duplicates.append(char)
            y = non_duplicates[0]
    print(y)

non_duplicate("minimum") 

# in "minimum", n and u are the only non-repeated characters
# but its asking to return the "first" non repeated character
