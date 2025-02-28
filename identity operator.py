#this type of operator deals with "is" and "is not"
name1="vasu"
name2="someshwar"
name3="somesh"
name4="vasu"
print(name1 is name2)#checking namea is same as name2
print(name2 is not name3)
print(name1 is name4)
print(name3 is not name2 or name2 is name3)
print(name3 is not name2 and name2 is name3)