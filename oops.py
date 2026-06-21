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
class Facotory:             # class name should be CAPITAL
    a = 12 # Attribute
    
    def hello(self):
        print("Hello world")
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
class Facotory:             
    def __init__(self,material,zips,pockets):          # Parameters ask from the user when the class call happens.
        # self keyword is used for targeting the location of obj1.
        # print(self)             # Facotory object at 0x0000019D7E046A50>(obj1)
                                # Facotory object at 0x0000019D7E2C8A50>(obj2)
        self.material = material
        self.zips = zips
        self.pockets = pockets
    
    def show(self):
        print(f"Your objects details are {self.material}, {self.zips},{self.pockets}")
    
        
obj1 = Facotory("leather",3,2)
obj2 = Facotory("nylon",3,3)
# print(obj1.pockets)
# print(obj2.pockets)

# obj1.show()
# obj2.show()

# -----------------------------------------------------------------------
# 
# --------- Types of Variables and Methods--------------

class Animal:
    name = "lion"       # class Attribute

    def __init__(self,age):
        self.age = age      # Instance Attribute
    def show(self):         # self represents targeting the object, so it is instance method.
        print("Hello this is self method")
        
    @classmethod
    def hello(cls):         # cls targets the location of the class.
        print("Hello this is class method")
        
    @staticmethod
    def static():           # Static methode
        print("It is static method")

obj = Animal(12)
# obj.show()
# obj.hello()         # The above cls is not targeting this object, it is targeting the Animal class.
# obj.static()
# obj.show()              # without using above self keyword, the error will occur.


