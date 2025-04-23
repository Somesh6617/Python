n=int(input("Enter the number: "))
num=n
c=0
if n==0:
    c=1
else:
    while n>0:
        n=n//10
        c+=1
print(f"No of digits in {num} is {c}")