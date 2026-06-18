# print("from today i will learn python consistently")

# ---------------------------------------------------------------

# variables

# name = "Hassan Zaheer"
# age = 22

# Differet cases for writing variables

# Pascal case
# StudentName = "Ali"     # the letter will be capital where space is required.

# Camel case
# studentName = "Ali"     # the first letter (word1) is small and the first letter (word2) will be capital.

# Snake case
# student_name = "ALi"    # all letter will be in small cases and undersoce(_) can be used.

# ------------------------------------------------------------------------------------------

# data types

# 1. int
# a = 34
# b = 4.5
# c = 12/4
# d = 15j

# print(type(a))      # int
# print(type(b))      # float
# print(type(c))      # Ans: float , because the numbers in p/q form will be treated as float.
# print(type(d))      # Ans: complex ; only j varibale is used for creating complex number in python.

# 2. strings

# a = "hassan"
# b = "23334"
# c = "@#$%%"

# print(type(a))      # str datatype
# print(type(b))      # str datatype
# print(type(c))      # str datatype


# 3. Boolean

# a = True
# c = False
# b = "True"      #string
# print(type(a))

# ----------------------------------------------------
# Strings
# Every character of string has its unicode and so it takes more space.

# a = "A"
# print(ord(a))     # to print unicode of character ( ord ) is used.

# a = 68
# print(chr(a))      # to convert from unicode to character

# Indexing

# a = "Hassan"
# print(a[1])
# print(a[-3], a[3])

# Negative Indexing : Starts from right end side (e.g n = -1 , a = -2)
# ------------------------------------------------------------------------

# String slicing

# a = "Hassan Zaheer"

# print(a[0:6:1])    #(start,end,stop)
# print(a[:6:])      # start = default = 0  , steps = default = 1    # same as above
# print(a[7:13:1])
# print(a[7::1])      # end = default = 1   # same as above
# print(a[7::])       # same as above
# print(a[::])        # print whole word

# -----------------------------------------------------------------------------------

# type convervion
# a = 12
# print(type(a))
# a = str(a)
# print(type(a))

# string -> int (vlaue should be only numeric)
# a = "12"
# print(type(a))
# a = float(a)
# print(type(a))

# a= 12
# print(bool(a))
# a = "Hassan"
# print(bool(a))
# b = 0
# print(bool(b))

# Falsy Values: (7 values) =  False, 0 , 0.0 , "" , [] ->empty list, () ->empty tuple, {} ->empty dictionary

# -------------------------------------------------------------------------------------------------------------------

# Implicit Conversion -> python automaticatically converts
# a = 12
# print(a/3)      # Ans: 4.0 (float) bcz it is in p/q form.

# ------------------------------------------------------------------------------
# Input & Output

# Output
# name = "Hassan"
# age = 21

# print(name,age)

# Formatted String method
# print(f"Hi my name is {name} And My age is {age}")

# Input
# input("What is your name ")
# name = input("What is your name ")
# print(name)

# age = int(input("What is your age "))
# print(age)

# Question 1
# number = int(input("Enter any number "))
# print(number)

# # Question 2
# age = int(input("Enter your age "))
# print(age)

# ----------------------------------------------------------------------------------------
# Operations

# Arithmatic Operators
# a = 5
# b = 20

# print(a+b)
# print(b-a)
# print(a*b)
# print(b/a)      # Ans: 4.0 (bcz of p/q form)
# (//) is used for floor division.
# print(b//a)     # Ans: 4 (converted into int type)

# print(7 ** 2)       # Exponential operator (power) e.g 7^2

# print( 5 ** 100)        # pyhton can give us large answers.

# print( 32 % 5 )         # Modulus operator will return remainder.

# Python follows BODMAS Rule.
# print( 12+6/2 )


# Assigment Operators

# basic operator is ( = )
# a = 45

# compound assignment operations

# a = 20
# print( a + 20 ) instead of this
# variables can be reassign so we will use this approach.

# a = a + 20
# a = a + 40
# print(a)  # Ans = 80
# a = a + 60
# print(a)  # Ans = 140

# we can also write the above lines.

# a += 20
# a += 40
# a += 60
# print(a)

# a -= 20
# a *= 20
# a /= 20
# a //= 20
# a **= 20

# Comparison operator -> always gives boolean results

# operators < , > , <=, >= , == , !=
# a  = 12.1
# b = 12

# print(a == b)       #True
# print(a != b)       #False

# print(a>b)
# print(45<50)

# print(23 > 23)      # False
# print(23 >= 23)      # True

# we can strings also using ascii values.
# print(ord("A"))
# print(ord("B"))
# print("A" >= "B")       # False

# print("ABC" > "ACD")    # on the basis of order/precedence as A == A , B == C , C == D

# Strings can only be compared with strings.It cannot compared with int values.
# print("A" > 34)     # Error will be occur


# Logical operators

# print(234 > 100 and 50 > 23 and 30 == 30)
# print(234 > 100 or 50 < 23 or 12 != 12)
# print(not 12 == 12)






