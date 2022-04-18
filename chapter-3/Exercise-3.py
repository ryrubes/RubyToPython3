# calculate which squaare you'll need to place a certain number of rice grains
# imagine you have a chessboard and put a single grain of rice on one square

# Exercise 3:
def chessboardSpace(numberOfGrains):
    chessboardSpaces = 1
    placedGrains = 1
# while placed grains are less that total number of grains, multiply by 2
# and move grain up one square
    while placedGrains < numberOfGrains:
        placedGrains *= 2
        chessboardSpaces += 1

    return chessboardSpaces

print(chessboardSpace(100))