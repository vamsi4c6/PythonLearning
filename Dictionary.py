d ={} #d = dict()
print(type(d))  # <class 'dict'>
print(d)

d[100] ="Vamsi"
d[200] ="Krishna"
d[300] = "is learning Python"

print(d)

d1 ={1:"Vamsi", 2:"Krishna", 3:"Srikakolapu"}
print(d1)

if(4 in d1):
    print("Key {} is present and value is {}".format(4, d1[4]))
else:
    print("Key {} is not present".format(4))

if(3 in d1):
    print("Key {} is present and value is {}".format(3, d1[3]))

print(d1.keys())
print(d1.values())


for k,v in d1.items():
    print("Key is {} and Value is {}".format(k,v))

d.update(d1) #all items from d1 will be copied to d
print(d)

del d1[2]
print(d1)

print(d.get(100)) 

d.clear()
print(d)

del d
print(d)
