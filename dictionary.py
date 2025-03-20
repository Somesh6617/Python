dic={'name':'vasu','RN':17,'age':20}
print(dic)
print(dic['name'])
print(dic['age'])
dic['sex']='M' #update()
print(dic)
#methods in dictionaries
print(dic.keys())
print(dic.values())
print(dic.items())
print(dic.pop('RN'))
print(dic)
print(dic.get('name'))
#looping
for i in dic:
    print(i)
for i in dic.values():
    print(i)
for i in dic.items():
    print(i)
for i,j in dic.items():
    print(i,j)
#comprehension
dic1={x:x*2 for x in range (1,6)}
print(dic1)