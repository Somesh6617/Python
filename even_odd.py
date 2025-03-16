#print even or odd numbers
#using for loop
n=int(input("Enter the number:"))
for i in range (1,n+1):
    if(i%2==0):
        print(f"{i} is even number")
    else:
        print(f"{i} is odd number")
#using while loop
print("Using while loop")
n=int(input("Enter the number:"))
i=1
while(i<=n):
    if(i%2==0):
        print(f"{i} is even number")
        i+=1
    else:
        print(f"{i} is odd number")
        i+=1

