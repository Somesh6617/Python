l=list(map(int,input("Enter the elements: ").split()))
key=int(input("Enter the key value :" ))
for i in l:
    if key-i in l:
        print("valid")
        break
    else :
        print("invalid")