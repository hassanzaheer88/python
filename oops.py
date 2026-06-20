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
    print("Hello I am getting initialized")

# Facotory()      # without this , the above class can be initializes.
# To access mehtods and attributes we use the Factory().
print(Facotory().a)
Facotory().hello()      # At first time all the things will be initialized. 
#   so "Hello I am getting initialized" will be print only one time.