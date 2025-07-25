name="  hello World "
name1="xyhello worldxy"
name2="100"
print(name.find("l")) # first occurance of a character
print(name.count('l')) # it counts the characters(repeated how many times the character is it repeated)
print(name.capitalize()) # it capitalizes only first character of a string
print(name.upper()) # it convers all the characters to uppercase
print(name.lower()) # it convers all the characters to lowercase
print(len(name)) # returns the length of a string
print(name.strip()) # removes first and last spaces
print(name1.strip("xy")) # removes the specified characters only from begining and ending (not in specified order)
print(name1.replace("xy","0")) # replace the specified characters with specified characters
print(name1*3) #prints the same characters in specified times
print(name1.isalpha()) # returns true if it is a single word else returns false
print(name2.isdigit()) # returns true if it is a digit
print(name1.startswith("xyH"))