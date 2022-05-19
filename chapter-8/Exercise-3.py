# function should return missing letter from alphabet
# should return f

from string import ascii_lowercase

def missing_letter(string):
    charset = ascii_lowercase
    for letter in charset:
        if letter not in string:
            print(letter)

missing_letter("the quick brown box jumps over a lazy dog")