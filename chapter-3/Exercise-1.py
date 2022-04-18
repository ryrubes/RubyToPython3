# Big O notation

# determine whether a given year is a leap year
# Exercise 1:
def isLeapYear(year):
    return (year % 100 == 0, year % 400 == 0, year % 4 == 0)

# feed the function any year, and see where its True or false indicating whether a leap year or not        
print(isLeapYear(2000))

# O(1) time complexity 