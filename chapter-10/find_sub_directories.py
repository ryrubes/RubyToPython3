

# Python method walk() generates the file names in a directory tree by walking
#  the tree either top-down or bottom-up.

# finds files and subdirectories in specified path
import os 

def find_subdirectories(target): 

    for root, dirs, files in os.walk(target):
        for x in dirs:
            print(root + "/" + x)
        break
         
find_subdirectories('/Users')