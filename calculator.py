num1=int(input("enter 1st element: "))
num2=int(input("enter 2nd element: "))
print("enter operation to be perform\n 1.addition(+) 2.subtraction(-) 3.multiplication(*) 4.division(/) 5.invalid operation/n :")
operation=input()
if operation == "addition" or operation=="+" or operation=="1":
    print(f"Sum of {num1} and {num2} numbers is :{num1+num2}")
elif operation=="subtraction"or operation=="-" or operation=="2":
    print(f"difference of {num1} and {num2} numbers is :{num1-num2}")
elif operation=="multiplication"or operation=="*"  or operation=="3":
    print(f"product of {num1} and {num2} numbers is :{num1*num2}")
elif operation=="division"or operation=="/" or operation=="4":
    if num2 != 0:
        print(f"division of {num1} and {num2} numbers is :{num1/num2}")
    else :
        print("denominator is cannot be zero")
else :
    print("invalid operation")

   
