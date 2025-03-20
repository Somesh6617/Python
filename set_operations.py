s1={1,2,3}
s2={2,3,4}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
#set membership
print(3 in s1)
print(4 in s1)
print(1 not in s2)
#set comprehension
s3={print(x) for x in range(6)}
s4={x for x in range (6)}
print(s4)
#frozen set. it is a immutable version of set
s5=frozenset(s1)
print(s5)
s5.add(5)
print(s5) #error because s5 cannot be modified(frozen set)