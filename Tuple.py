#List is mutable whereas tuple is immutable. Mutable means we can change the
#elements of the list but in tuple we cannot change the elements once it is created.

t=(10)
print(type(t))  #int type

t=(10,)
print(type(t))  #tuple type

 
t=tuple(range(10,20,2))   
print(t)   

t=(10,20,30,10,50,10,30)
print(t.count(10))  #counts how many times 10 is present in the tuple
print(t.index(30))  #gives the index of first occurrence of 30 in the tuple

print(sorted(t))  #returns a sorted list of the tuple elements
print(sorted(t,reverse=True))  #returns a sorted list in descending order