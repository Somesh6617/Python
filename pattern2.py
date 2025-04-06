for j in range(5,0,-1):
    print("*"*j)
    #or
n=int(input("Enter no.of rows: "))
for i in range (n,0,-1):
    for j in range (i):
        print("*",end=" ")
    print()