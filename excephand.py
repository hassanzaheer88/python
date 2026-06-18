# -------------------- Exception Handling -------------------------------------

# Error:
# Syntax Error
# print("hello"             # SyntaxError: '(' was never closed

# Indentation Error
# a = 12
# if a==12:
# print("Hello")          # IndentationError: expected an indented block after 'if' statement
# These errors cannot be handled. 

# The other errors are known as Exceptions. And these can be handled.

a = int(input("ENter any number: "))
print(10/a)                 # ZeroDivisionError: division by zero: Known as Exception.
print("Okay I have done division")








