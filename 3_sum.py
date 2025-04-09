l = list(map(int, input("Enter the elements: ").split()))
key = int(input("Enter the key value: "))
res = 0 
for i in l:
    for j in l:
        for k in l:
            if i + j == key:
                res = 1  
                break
        if res == 1:
            break

if res == 1:
    print("Key is present")
else:
    print("Key is not available")
