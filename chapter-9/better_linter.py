chars = ["(", "[", "{", "}", "]", ")"]
inputt = "([{}])"


# Built-in all() method to get rid of the 2nd loop. This method checks if
# all booleans are True
complete_brackets = all([char in inputt for char in chars])

if complete_brackets == True:
	print("brackets are complete")
else:
	print("theres a missing bracket")

for i in inputt:
	for char in chars:
# check for opening braces
		if "(" not in inputt:
			print("you're missing a opening parentesis")
			break

		if "[" not in inputt:
			print("you're missing a opening square brace")
			break

		if "{" not in inputt:
			print("you're missing a opening squiggly brace")
			break

# check for closing braces
		if "}" not in inputt:
			print("you're missing a closing squiggly brace")
			break
			

		if "]" not in inputt:
			print("you're missing a closing square brace")
			break
			

		if ")" not in inputt:
			print("you're missing a closing parentesis")
			break

	break
