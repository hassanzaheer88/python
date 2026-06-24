

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





