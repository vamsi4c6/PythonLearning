'''List objects are dynamic. i.e based on our requirement we can increase and decrease the 
size. 
 
append(),insert() ,extend() ===>for increasing the size/growable nature 
remove(), pop() ======>for decreasing the size /shrinking nature
'''

l1 = [10,20,30,40,50]
print(l1)
print(type(l1))


#l2 = eval(input("Enter list elements: "))
#print(l2)
#print(type(l2))


l3 = list(range(0,11,5))
print(l3)  
print(type(l3))

name = "My name is Vamsi Krishna Srikakolapu"
l4 = list(name.split())
print(l4)

print(l4[1:3]) #this is slicing of list. 

#2 ways to iterate over list
#1. using direct element access
for item in l4:
    print(item)
#2. using index
for i in range(len(l4)):
    print("Element at {} is {}".format(i,l4[i]))

l4.append("Hello")
print(l4)

l4.insert(3,"Venkata")
print(l4)

l4.insert(4,"Satya")
print(l4)

l4.remove("Hello")
print(l4)

print(l4.pop())
print(l4)

print(l4.pop(2))
print(l4)


l5 = ["Dog","Banana","Apple","Cat","Orange"]

l5.sort()
print(l5)

l5.reverse()
print(l5)

#= operator meant for aliasing 
#copy() function meant for cloning 
l6 = [10,20,30,40,50,60,70,80,90,100]
l7 = l6
print(l6)
print(l7)

l7[4] = 200

print(l6)
print(l7)

l8 = [10,20,30,40,50,60,70,80,90,100]

l9 = l8.copy()

print(l8)
print(l9)

l9[4] = 300

print(l8)
print(l9)

l10 = [1,2,3]
l11 = [4,5,6]

print(l10+l11)

print(l10*3)

print(l10.clear())

print(l10)

#nested lists
n=[10,20,[30,40]]   
print(n)   
print(n[0])   
print(n[2])   
print(n[2][0])   
print(n[2][1])   

#Nested list as matrix
n=[[10,20,30],[40,50,60],[70,80,90]]   
print(n)   
print("Elements by Row wise:")   
for r in n:   
    print(r)   
print("Elements by Matrix style:")       
for i in range(len(n)):   
    for j in range(len(n[i])):   
        print(n[i][j],end=" ")   
    print()
              