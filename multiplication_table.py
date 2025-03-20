n=int(input("Which table do you want ? : "))
i=1
print("Enter which loop do you want to use either WHILE or FOR loop :")
loop_selection=input()
if(loop_selection=="WHILE" or loop_selection=="while" ):
    while i<11:
        print(f"{n} X {i} = {n*i} ")
        i+=1
elif(loop_selection=="FOR" or loop_selection=="for"):
    for i in range (1,11):
        print(f"{n} X {i} = {n*i} ")
else:
    print("Invalid loop")
