n=int(input("Enter the number : "))
print("Enter which loop do you want to use either WHILE or FOR loop :")
loop_selection=input()
factorial=1
if(loop_selection=="WHILE" or loop_selection=="while" ):
    i=1
    while i<=n:
        factorial*=i
        i+=1
    print(f"{n} factorial is {factorial} ")
elif(loop_selection=="FOR" or loop_selection=="for"):
    i=1
    for i in range (1,n+1):
        factorial*=i
    print(f"{n} factorial is {factorial} ")    
else:
    print("Invalid loop")