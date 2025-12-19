# 4 types - Positional arguments, Keyword arguments, Default arguments, Variable-length arguments

# Positional arguments
def greet(name, msg):
    print("Hello {}, {}".format(name, msg))

greet("Vamsi", "Good Morning")

# Keyword arguments
greet(msg="Good Evening", name="Krishna")

# Default arguments
def greet_default(name, msg="How are you?"):
    print("Hello {}, {}".format(name, msg)) 

greet_default("Vamsi")
greet_default("Krishna", "Welcome back!") 

#variable-length arguments
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all())
print(sum_all(1, 2, 3))
print(sum_all(10, 20, 30, 40, 50))

#position of these arguments are as follows - Positional, Default, *args, Keyword
