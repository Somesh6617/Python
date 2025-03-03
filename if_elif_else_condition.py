"""it deals eith multiple conditions
if the if condition is false it checks all elif conditions if any one of condition is true it executes the block of code present in that satisfied condition 
else executes else condition code"""
x=int(input("enter the number: "))
if(x<10) :
    print("Number lesser than 10")
elif x>10 :
    print("Number greater than 10")
else :
    print("invalid number")
print("code done")