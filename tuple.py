t=(1,2,"good",3,4,"morning",[5,6,7],(8,9),3)
print(t)
print(t.index([5,6,7]))
print(t.index("good"))
print(t.count(3))
print(len(t))
print(t[::-1])
print(t[0:5:2])
for i in range (len(t)):
    print(t[i])