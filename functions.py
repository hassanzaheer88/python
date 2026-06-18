
# def hello():
#     print("This is a hello function")

# hello()

# def sum():
#     print("This is the sum function")
# sum()

# the thing you accept = Parameters
# The thing you provide to the parmeters  = arguments

# def sum(a,b):
#     print(f"The answer of sum function is {a+b}")

# sum(12,12)
# sum(32,32)    # these are called positional arguments.

# The purpose of function is to make reuseable.
# e.g a=12 , b=12 to print sum # print(a+b) but if we want some of other numbers then
# we have to again create new variables c = 23 , d=23 and we have to write again printf(c+d).
# so funtion gives us easiness by providing reuseable component.


# parameters = arguments but we have some other arguments.
# ------------------------------------------------------------------------------------------------------

#--------- Types of Arguments-------------------
# 3 types of Arguments

# 1. discussed above
# 2. Keyword Argument
# def hello(name,age):
    # print(f"the name is {name} and age is {age}")

# hello("Hassan",22) #  positional
# hello(22,"Hassan") # Answer will be wrong , name = 22 , age = Hassan
# hello(age=22,name="Hassan")     # known as keyword argument.

# 3. Default Argument

# def sum(a,b):
#     print(f"The sum is {a+b}")

# sum(23,34)        # As discussed above

# So we can write default argument as below.

# def sum(a,b=40):        # b=40 default parameter
#     print(f"The sum is {a+b}")

# sum(23)         # here b = default parameter = 40
# sum(23,23)      # b=23 will replace the value of b = 40


# def palindorm(st):
#     rev = ""
#     for i in range(len(st)-1,-1,-1):
#         rev = rev + st[i]
        
#     if rev == st:
#         print(f"{st} is Palindrome")
#     else:
#         print(f"{st} is Not Palindrome")
        
# palindorm("naman")
# palindorm('cursor')


# --------------------------------------------------------------
# Return in function:

def hello():
    return "Hello World"       # return: it returns the value to the place where function is called.

hello()             # so to print "Hello World" we have to print the call function.
print(hello())      # output: "hello world"
