#maximum and minimum element in list
l=[1,11,13,1,1]
l.sort()
print(f"min={l[0]} and max={l[len(l)-1]}")
  #another way
"""l=[1,11,13,1,1]
max=min=l[0]  
for i in range (len(l)-1):
    if(l[i]>max):
        max=l[i]
    if(l[i]<min):
        min=l[i]
print(f"max={max} and min={min}")"""
