l=[1,2,'hello',2,3,7,"hi",5,3]
l1=[2,4,1,3,5,3,8]
t=[1,2,"good",3,4,"morning",[5,6,7],(8,9)]
print(t)
print(l)
l.append(4)
print(l)
l.insert(0,5)
print(l)
print(len(l))
print(l.count(3))
l.reverse()
print(l)
print(l[::-1])
print(l1.remove(5))
l1.sort()
print(l1)
print(len(l),l1[0])
for i in range (len(l)):
    print(l[i])
print("   ",l.index("hi"))