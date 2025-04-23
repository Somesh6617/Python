n=int(input("Enter the number: "))
num=n
quo=0
if n==0:
    print("0 is an armstrong number ")
else:
    while n>0:
        rem=n%10
        quo=quo+rem**3
        n//=10
    if quo==num:
        print(f"{num} is an armstrong number")
    else:
        print(f"{num} is not an armstrong number")