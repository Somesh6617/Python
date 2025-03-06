"""a=int(input("enter a value: "))
b=int(input("enter b value: "))
a,b=b,a
print(f"a value:{a},bvalue:{b}")"""
a,b=1,2
a+=b
b=a-b
a-=b
print(f"a value:{a},b value:{b}")