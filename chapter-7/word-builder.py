def worldBuilder(array):
    collection = []

    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:
                collection.append(array[i] + array[j])
    
    return collection

print(worldBuilder(["a", "b", "c", "d"]))