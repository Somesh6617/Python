#set
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(f"Intersection: {s1.intersection(s2)}\nUnion: {s1.union(s2)}")
#dictionary
dic={'Name':'Vasu','Age':'19','City':'America'}
dic['Age']=18
dic['City']='London'
for i,j in dic.items():
    print(f"{i}:{j}")
#list
l1=[1,2,3,4]
l2=[5,6,7,8]
print(l1+l2)#concatination
#list comprahension
l3=[x**2 for x in range (1,6)]
print(l3)
