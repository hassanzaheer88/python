

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
# def addition(a,b,c,d):      # here any number of prameters cab take.
#     print(f"Sum is {a+b+c+d}.")
    
# addition(34,21,2,3)

# ---------------------------------------------------------------------



# Termary Operation
# a = 12
# print("even") if a%2==0 else print("Odd")

# ------------ Comprehension Method -----

# Usual  method
# l = []
# for i in range(1,21):
#     if i%2 == 0:
#         l.append(i)

# print(l)  
# These 4 to 5 lines can be reduced to 1 line.

# --------- List Comprehension -------------
# structure: [variable(needed to be append) loop if condition]

# l = [i for i in range(1,21) if i%2==0 ]
# print(l)

# ------------- Dictionary Comprehension ------------

# l = {i:i**2 for i in range(1,10)}
# print(l)

# -------- Set Comprehension ------------------------

# l = {x*x for x in range(1,11) if x%2==0}
# print(l)

# ------------------------------------------------------

# ------------------- lambda Functions ------------------ 

# A ususal method: 

# def addition(a,b):
#     print(a+b)
    
# addition(2,3)

# lambda function is used to write the above function in 1 line.
# lambda expression should always be stored in variable. Then that variable will become object and we can use this object anywhere.

# addition = lambda a,b : print(a+b)
# addition(2,3)
# ----------------------------------------------------

# addition = lambda a : "even" if a%2 == 0 else "odd"
# print(addition(22))

# ------------------------------------------------------

# --------- Map, filter ------------------

# a = [1,2,3,4,5]

# res = map(lambda x: x*2,a)
# print(res)      # Output: <map object at 0x0000014E7494B7C0>
# print(list(res))

# ----------- we can also use function ------------


# a = [1,2,3,4,5]

# def double(x):
#     return x*2

# res = map(double,a)
# print(list(res))


# ------------------------ filter ----------------

# filter works on True and false.

# def even(x):
#     if x%2 == 0:
#         return True
#     else:
#         return False
    
# a = [1,2,3,4,5,6]
# result = filter(even,a)
# print(list(result))


# -------------------------------------------------

# a = [1,2,3,4,5,6]
# result = filter(lambda x : True if x%2==0 else False , a )
# print(list(result))

# ------------------------------------------------------

# ------------- Modules and Packages -------------------

# modules = import another file.

# I have created maths.py so import here and use it's function. this is known as Modules.

# import maths
# ans = maths.addition(12,14)
# print(ans)

# I can access functions directly.

# from maths import addition
# print(addition(23,34))

# ----------- In-build Modules ------------------

# import math
# print(math.sqrt(4))

# --------------- Packages --------------------

# A package is a folder that contains one or more modules.

# Import from One folder that is from packages.

# from packages import hello
# from packages import hello,maths1

# --------------------------------------------------------------

# Import from SubFolder.
# from packages.packages1 import hello,maths1

# ----------------------------------------------------------------