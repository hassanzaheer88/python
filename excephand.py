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

# a = int(input("ENter any number: "))
# print(10/a)                 # ZeroDivisionError: division by zero: Known as Exception.
# print("Okay I have done division")


# Now we to Handle these Exceptions , we use Try else method.

# a = int(input("ENter any number: "))
# a = input("ENter any number: ")      # Sorry there is an Error as unsupported operand type(s) for /: 'int' and 'str'
# try:
#     print(10/a)
# except Exception as err:
#     print(f"Sorry there is an Error as {err}")
# else:               # it will run when NO exception occurs.
#     print("Good everything is working.")
# finally:            # It will run always, wheather there's exception or not.
#     print("Final block Execution")
    
# print("Okay I have done division")


# Raise keyword Usecase: throwing error manually

# age = int(input("ENter your age: "))

# try:
#     if age<10 or age>18:
#         raise ValueError("Your age must be between 10 and 18.")
#     else:
#         print("Welcome to the college")
# except Exception as err:
#     print(f"An error occured as {err}")
    
# print("The college will open soon")




