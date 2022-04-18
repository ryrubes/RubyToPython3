# accepts an array of strings and returns a new array that only contain strings that start with the character "a"

# Excersice 4:
def selectAStrings(array):
    newArray = []
    i = 2
    if array[i].startswith("a"):
        newArray.append(array[i])
    return newArray

print(selectAStrings(["hello", "testing testing", "a aye!", "a!"]))