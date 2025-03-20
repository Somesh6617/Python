N=int(input("Enter the number: "))
for i in range (1,N+1):
    if(i==5):
        print("loop breaking at ",i)
        break
    else:
        print(i)