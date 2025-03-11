str=" Hello World "
str1="hhellow Wworlldd"
str2="ayayllo lloayay"
print(str.lower())#str.lower() method is used to convert all letters into lowercase
print(str.upper())#str.upper() method is used to convert all letters into uppercase
print(str.strip())#str.strip() method is used to remove the leading and trailing white spaces
print(str1.strip('h,d'))# str.strip() method removes the letters given in strip(present in begining and last,begining or last)
print(str2.strip('ay'))# str.strip() removes the letters given in strip(present in begining and last,begining or last)
print(str2.replace('y','b'))#str.replace() method is used to replace the given first letter with second letter
print(str2.count('a'))#str.count() method is used to count the no.of repeated letters as mentioned in method(count())
print(str2.capitalize())#str.capitalize() method is used to capitalize the first letter of the given string