N=int(input("Enter the number: "))
for i in range (1,N+1):
    if(i%2==0):
        print("It skips iteration ",i)
        continue
    else:
        print(i)