#remove dubilicate elements in list
"""ele=input("Enter the list : ").split(",")
l=[int(item) for item in ele]
nl=[]
for i in l:
    if i in nl:
        continue
    else:
        nl.append(i)
print(nl)"""
l = [1, 2, 3, 2, 4, 1]
s=list(set(l))#converting to set and after converting to list
print(s)