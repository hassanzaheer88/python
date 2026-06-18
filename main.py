#print("Today we are learning python")

# a = 65
# b = "Hassan Zaheer"
# c = True
# d = 5j ------ #complex data type (only j symbol is allowed)

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# ---------------------------------------------
# Unicode

# unicode = "A"
# print(ord(unicode)) #ord() will print unicode

# character = 80
# print(chr(character))

# -------------------------------------------------
# String indexing

# name = "Hassan"
# print(name[1],name[-1])

# ---------------------------------------------------
# String Slicing 

# slice = "Python Machine learning"
# print(slice[:6:]) #start = default=0
# print(slice[7:15:1])
# print(slice[15::1]) #end = default = end
# print(slice[9:14:]) #steps = default = 1

# ------------------------------------------------------
# Type Conversion

# a = "123"
# a = str(a)
# print(type(a))
# print((a))

# b = "abc"
# b = bool(b) #explicit  conversion
# print(b)

# bool() will return false for these 7 things: false,0,0.0,"",[],{},()
# -----------------------------------------------------------------------------

# implicit conversion VS explicit conversion
# a = 12
# print(a/3) #implicit conversion because of divion symbol
# ----------------------------------------------------------------------------
# Output:
# name = "HASSAN"
# age = 21
# print("My name is ",name,"And my age is",age)
# # output using a formatted string
# print(f"My Name is {name} and My Age is {age}") 
 
# Input:

# name = input("Enter your name ? ")
# print("Name:",name)

# age = int(input("Enter your age ? "))
# print("Age:",age)

# Question
# 1.
# numbers = int(input("Enter the numbers: "))
# print(numbers)
# # 2.
# age = int(input("Enter age: "))
# print(age)

# --------------------------------------------------------------
# Operators

# Arithmatic Operators

# a = 12
# b = 10
# print("Addition: ",a + b)
# print("Subtraction: ",a - b)
# print("Division: ",a / b)
# print("FLoor Division: ",a // b) # floor divion
# print("Exponential: ",a ** b) # power/exponential
# print("Modulus: ", a % b) # modulus

# # python folows BODMAS Rule
# print("BODMAS Rule: ", 3 + 15/3 - 1)
# ----------------------------------------------------
# Compound Assignmnet Operations:

# a = 30
# a += 10     # a = a + 10 -> 40
# a += 20     # a = a + 20 -> 60
# a += 30     # a = a + 30 -> 90
# print(a)

# -------------------------------------------------
# Comparison Operators

# a = 10
# b = 10
# print(a == b)
# print(a != b)
# print(a > b)
# print(a >= b)
# print(a < b)
# print(a <= b)
# print(ord("A"))
# print("A" > "B")
# print("ABC" > "BAE")      # checks A>B , B>A , C>E
#print("A" > 56)     #  error because of different datatypes

# Logical Operators:

# print(55 == 55 and 21>20 and 10<=10)
# print(55 == 45 or 21<20 or 10<10)
# print(not 20!=20)

# -------------------------------------------------------------------

# Questions:
# print((456 == 456) != (235 == 236) ) 
# print(True and bool(0))

# ---------------------------------------------------------------------