#count the number
elements=input("Enter the elements: ").split(" ")
l=[int(item) for item in elements]
num=int(input("enter the element to count: "))
count=l.count(num)
print(f"count of {num} = {count}")
    #another method
"""elements=input("Enter the elements: ").split(" ")
l=[int(item) for item in elements]
count=0
num=int(input("enter the element to count: "))
if(num not in l):
    print("invalid element")
else:
    for i in l:
        if num==i:
            count+=1
    print(f"count of {num} = {count}")"""