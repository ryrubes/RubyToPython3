# palindrome is a word or phrase that reads the same both forward and backward

def isPalindrome(string):
    # start the left index at 0
    leftIndex = 0
    # start right index at last of array
    rightIndex = string[-1]
    # iterate until leftIndex reaches the middle of the array
    while leftIndex < len(string) // 2:
            if str([leftIndex] != str([rightIndex])):
                return False

            # move left index one to the right 
            leftIndex += 1
            # move rightIndex to the left
            rightIndex -= 1

    return True

    #print(isPalindrome(["racecar"]))

print(isPalindrome(["racecar"]))

