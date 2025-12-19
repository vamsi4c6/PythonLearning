#2 types  - Built-in functions and User-defined functions

def add(a,b):
    return a+b
print(add(10,20))
print(add("Vamsi ","Krishna"))

def wish(name):
    print("Hello {}, Good Morning".format(name))

wish("Vamsi")
print(wish("Krishna"))

def square(n):
    return n*n
print(square(5))


#function to define whether a number is even or odd)
def even_odd(n):
    if(n%2==0):
        return "Even"
    else:
        return "Odd"
    
print(even_odd(10))
print(even_odd(7))

#function to find factorial of a number
def factorial(n):
    fact =1
    for i in range(1,n+1):
        fact = fact * i
    return fact

print(factorial(5))

#python can return multiple values from a function
def sum_diff(a,b):
    sum = a+b
    diff = a-b
    return sum,diff

s,d = sum_diff(10,5)
print("Sum is {} and Difference is {}".format(s,d))