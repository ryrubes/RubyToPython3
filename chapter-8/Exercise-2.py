# returns the first duplicate value it finds

def find_duplicate(array_of_strings):
    duplicates = []

    for char in array_of_strings:
        if array_of_strings.count(char) > 1:
            if char not in duplicates:
                duplicates.append(char)
            else:
                continue
    print(duplicates)

find_duplicate(["a", "b", "c", "d", "c", "e", "f"])