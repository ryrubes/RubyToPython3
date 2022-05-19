#function that uses a stack to reverse a string

def rev_string(input):
    stackkk = []
    for i in input:
    # add each element to stack
        stackkk.append(i)
    stackkk.sort(reverse=True)
    print(stackkk)

rev_string("abcdefg")





