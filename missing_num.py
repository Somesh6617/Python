l=list(map(int,input("Enter thr elements: ").split()))
le=len(l)
s=0
for i in range (0,le):
  s=s+l[i]
t=(le*(le+1))//2
print(f"Missing number is {s-t}")