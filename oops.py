# -------------------- Object Oriented Programming ------------------------------

# ----------- Imperative Approach -----------
# a = 12
# b = 23
# print( a + b ) 

# ------------ Functional Approach --------------
# def sum(a,b):
#     print( a + b )

# sum(12,34)
# sum(4,54)

# --------------- Object Oriented Approach ---------------

# Advantages : 1. Code reuseable , 2. Execute mutiple things at same time 
# 3. Provides Security 4. Works well for Management System (bank management ,library management)

# -------------- Classes in OOPs ------------
# class Facotory:             # class name should be CAPITAL
    # a = 12 # Attribute
    
    # def hello(self):
    #     print("Hello world")
    #print("Hello I am getting initialized")

# Facotory()      # without this , the above class can be initializes.
# To access mehtods and attributes we use the Factory().
# print(Facotory().a)
# Facotory().hello()      # At first time all the things will be initialized. 
#   so "Hello I am getting initialized" will be print only one time.

# ------ Objects --------

# obj = Facotory()        # obj = object , it has all the powers of class.
# print(obj.a)
# obj.hello()
# obj2 = Facotory()
# obj3 = Facotory()


        
# Constructors are used to accept parameters from the user.
# class Facotory:             
#     def __init__(self,material,zips,pockets):          # Parameters ask from the user when the class call happens.
#         # self keyword is used for targeting the location of obj1.
#         # print(self)             # Facotory object at 0x0000019D7E046A50>(obj1)
#                                 # Facotory object at 0x0000019D7E2C8A50>(obj2)
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets
    
#     def show(self):
#         print(f"Your objects details are {self.material}, {self.zips},{self.pockets}")
    
        
# obj1 = Facotory("leather",3,2)
# obj2 = Facotory("nylon",3,3)
# print(obj1.pockets)
# print(obj2.pockets)

# obj1.show()
# obj2.show()

# -----------------------------------------------------------------------
# 
# --------- Types of Variables and Methods--------------

# class Animal:
#     name = "lion"       # class Attribute

#     def __init__(self,age):
#         self.age = age      # Instance Attribute
#     def show(self):         # self represents targeting the object, so it is instance method.
#         print("Hello this is self method")
        
#     @classmethod
#     def hello(cls):         # cls targets the location of the class.
#         print("Hello this is class method")
        
#     @staticmethod
#     def static():           # Static methode
#         print("It is static method")

# obj = Animal(12)
# obj.show()
# obj.hello()         # The above cls is not targeting this object, it is targeting the Animal class.
# obj.static()
# obj.show()              # without using above self keyword, the error will occur.


# ----------- Inheritance ------------------------

# class Factory:       # parent class/ super class
#     a = "I am an attribute in Factory class"
#     def hello(self):
#         print("I am a method inside Factory class")

# class Factory2(Factory):       # child class/sub class , it has inherited whole Factory class.
#     pass

# obj = Factory()           # it can access all the attributes and methods of Factory class.
# obj2 = Factory2()         # instance of child class.
# print(obj.a)
# obj2.hello()         # Output: I am a method inside Factory class

# -------- Constructor in Inheritance ------------

# class Animal:
#     def __init__(self,name):
#         self.name = name        # instance attribute
#     def show(self):
#         print(f"Hello your name is {self.name}")
#         print(f"Hello your name is {self.name}, {self.age}") # Error: when parent class method is called.
        

# class Human(Animal):    # It has also inherited the power of constructor function.
#     def __init__(self, name,age):
#         super().__init__(name)                    # super() targets the parent class.
#         self.age = age
#     def show(self):     # method overriding
#         print(f"Hello your name is {self.name}, {self.age}")
        
# animal1 = Animal("lion")        # instance of parent class
# person1 = Human("Ali")          # instance of child class
# person1.show()                  # Output: Hello your name is Ali

# animal1 = Animal("lion")
# person2 = Human("ALi",23)
# person2.show()              # Output: Hello your name is ALi, 23 (age is initialized in child class) 
# animal1.show()                 # Output: Error: 'Animal' object has no attribute 'age',
# So we should create show() of the child for itself.



# -------------- Types of INHERITANCE -----------

# ----- Multiple Inheritance -------
# class Animal:
#     name1 = "lion"
# class Human:
#     name2 = "Harsh"
# class Robot(Animal,Human):      # It's object will target names of first Animal,then Human.
#     name3 = "charlie"
    
# obj = Robot()
# print(obj.name1)
# print(obj.name2)
# print(obj.name3)

# -------------------------------
# class Animal:
#     def __init__(self,name):
#         pass
# class Human:
#     def __init__(self,name,age):
#         pass
    
# class Robot(Animal,Human):      
#     name3 = "charlie"
    
# obj = Robot()       # Here Robot() is asking only name from us, so it is targeting Animal class.
# because Animal class is written first in order.

# Note - The constructor function will be inherited of the first 
# class that has been Inherited. This is MRO(Method Resolution 
# Order) followed by python.

# So if we want to ask bot name and age then we will change the order as below:

# class Robot(Human,Animal):      
#     name3 = "charlie"
    
# obj = Robot()       # Now it is asking both name and age.


# ------- Multilevel Inheritance -----------
# class Factory:      # Grandparent Class
#     def __init__(self,material,zip):
#         self.material = material
#         self.zip = zip
# class Factory2(Factory):    # Parent class
#     def __init__(self,material,zip,color):
#         super.__init__(material,zip)
#         self.color = color
# class Factory3(Factory2):       # Child CLass
#     def __init__(self,material,zip,color,pockets):
#         super.__init__(material,zip,color)
#         self.pockets = pockets

# obj = Factory3()        # material: Any, zip: Any, color: Any, pockets: Any

# --------------------- Hierarchy Inheritance ---------------
# Two child class will inherit the one parent class methods and attributes.

# ------------------------------------------------------------------------------



