n=int(input("Enter the number: "))
num=n
quo=0
if n==0:
    print("0 is palindrome ")
else:
    while n>0:
        rem=n%10
        quo=quo*10+rem
        n//=10
    if quo==num:
        print(f"{num} is palindrome")
    else:
        print(f"{num} is not a palindrome")