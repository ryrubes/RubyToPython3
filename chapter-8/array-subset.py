
from multiprocessing import Value


def isSubset(array1, array2):
    largerArray = ["a", "b", "c", "d", "e", "f"]
    smallerArray = ["b", "d", "f"]
    hashTable = {}

    if len(array1) > len(array2):
        largerArray = array1
        smallerArray = array2
    else:
        largerArray = array2
        smallerArray = array1

    for i in range(len(largerArray)):
        hashTable[Value] = True

    for i in range(len(smallerArray)):
        if hashTable[Value]:
            return False

    else:
        return True

print(isSubset(["a", "b", "c", "d", "e", "f"], ["b", "d", "f"]))

