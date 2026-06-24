

# ------------------ Dunder Methods --------------------

# Dunder= double underscore

# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"Hello how are you {self.name}"
#     def __add__(self, other):           # other is used for obj2.
#         return f"The sum is {self.age + other.age}"

# obj = Animal("Lion",12)
# obj2 = Animal("Dolphin",14)
# # print(obj)                  # For Dunder methods, we have to just print(object).
# print(obj + obj2)               # Output: The sum is 26

# For more than Two objects we will use Tuple.

# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"Hello how are you {self.name}"
#     def __add__(self, other):
#         sum = 0
#         for i in other:    
#             sum = sum + i.age              # i = locations of other([obj2],[obj3],..)
#         return f"The sum is {self.age + sum }"

# obj = Animal("Lion",12)
# obj2 = Animal("Dolphin",14)
# obj3 = Animal("Cat",5)

# print(obj + (obj2,obj3))        # Output: The sum is 31

# ---------- Decorator -------------------------

# class Animal:
#     @property
#     def show(self):
#         print("Hello how are you ")

# obj = Animal()
# # obj.show()          # Hello how are you
# obj.show            # Hello how are you , because of use of decorator. @property
# ---------------------------------------------------------------------------------------------
 
# def decorator(func):
#     def wrapper():
#         print("I will run before the Function")
#         func()
#         print("I will run after the Function")
#     return wrapper


# @decorator
# def hello():
#     print("Hello How are you? ")
    
# hello()

# ----------------------------------------------------

# When parameters are used in functions.

# def decorator(func):        # It takes actual function . Here func = hello()
#     def wrapper(a,b):       # It takes parameterrs.
#         print("The addition to your numbers are")
#         func(a,b)
#         print("Thank you")
#     return wrapper


# @decorator
# def addition(a,b):
#     print(f"Sum is {a+b}.")
    
# addition(34,21)


# ------------------------------------------------------------

# args: is used for capturing multiple arguments.

# def addition(a,b,c,d): # at each time ,we have to write arguments.
#     print(a+b+c+d)

# addition(2,3,5,6)

# so *args is used for capturing multiple arguments.

# def addition(*a):
#     sum = 0
#     for i in a:
#         sum = sum + i
    
#     print(sum) 

# addition(2,3,5,6,34,5,532,32,2,3,23,3,4,5,552,32)

# Kwargs: is used for capturing keyword(key values) arguments.

# def addition(**kwargs):
#     print(kwargs)

# addition( a= 12, c=24, d=34)        # keword aguments: a = 12 ,b = 23
# # Output: {'a': 12, 'c': 24, 'd': 34}

# --------------------------------------------------------------------------------

# def information(**kwargs):
#     print("Your Information is\n")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")

# information(name = "Akash",age = 23, designation = "Ai/ML")
# -------------------------------------------------------------------

# Use In Decorators

# def decorator(func):       
#     def wrapper(*args,**kwargs):       
#         print("The addition to your numbers are")
#         func(*args,**kwargs)
#         print("Thank you")
#     return wrapper


# @decorator
# def addition(a,b):
#     print(f"Sum is {a+b}.")
    
# addition(34,21)

# ---------------------------------------------------------------------



