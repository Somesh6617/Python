n1=int(input("Enter n1: "))
n2=int(input("Enter n2: "))
c=0
m=min(n1,n2)
if (n1==0 or n2==0):
    print("it not contain divisors")
else:
    for i in range (1,m+1):
        if(n1%i==0 and n2%i==0):
           c=i
    print(f"GCD of {n1},{n2} is {c}")