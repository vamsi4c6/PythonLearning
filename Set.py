s = {10,20,30,40,50}
print(s)
print(type(s))
s.add(60)
print(s)
s.add(30)  #adding duplicate element has no effect
print(s)

l = [10,20,30,40,50,10,20]
s2 = set(l)
print(s2) #duplicates are removed when converting list to set

s3 = set(range(10,21)) #creates set from range
print(s3)

s.update(l,range(0,10,2)) #adds elements from list l and range to set s
print(s)

print(s.remove(20)) #removes 20 from set s. returns error if element not found
print(s)

print(s.discard(100)) #does not throw error if element not found
print(s)

print(s.pop()) #removes and returns an arbitrary element from the set
print(s)

print(s.clear()) #removes all elements from the set

x ={1,2,3}
y ={3,4,5}
print(x.union(y)) #returns union of sets x and y
print(x.intersection(y)) #returns intersection of sets x and y
print(x.difference(y)) #returns elements in x but not in y
print(x.symmetric_difference(y)) #returns elements in either x or y but not in both