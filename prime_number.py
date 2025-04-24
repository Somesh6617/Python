n=int(input("Enter the number: "))
c=0
if n==0 or n==1:
    print(f"{n} is not a prime number")
else:
    for i in range (1,n+1):
        if(n%i==0):
            c+=1
    if c==2:
        print(f"{n} is prime number")
    else:
        print(f"{n} is not a prime number")