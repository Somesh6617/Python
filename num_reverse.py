n=int(input("Enter the number: "))
num=n
quo=0
if n==0:
    print("Number cannot be reversed")
else:
    while n>0:
        rem=n%10
        quo=quo*10+rem
        n//=10
    print(f"{num} after reversing is {quo}")