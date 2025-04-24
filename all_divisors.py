n=int(input("Enter the number: "))
if n==0:
    print("No divisors for 0")
else:
    print(f"The divisors of {n} are :")
    for i in range (1,n+1,1):
        if(n%i==0):
            print(i)