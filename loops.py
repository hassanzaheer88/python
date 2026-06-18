# for loop:

# a = range(2,18,1)
# for i in a:
#     print(i)

# for i in range(1,21,1):
#     print(i)

# for i in range(21):       #start = default = 0 , step = default = 1
#     print(i)

# inverse for loop
# for i in range(16,0,-1):
#     print(i)

# from -5 to -15
# for i in range(-5,-16,-1):
#     print(i)

# print a table of 5

# for i in range(5,5*10+1,5):
#     print(i)


# n = int(input("Enter the number for Table: "))
# for i in range(n,(n*10)+1,n):
#     print(i)

# 1. method
# a = "Government College University"
# print(len(a))

# for i in range(len(a)):
#     print(a[i])

# for i in range(3):
#     print("python")

# 2. method
# a = "Government College University"
# for i in a:
#     print(i)

# Break , Continue , Else Statments:

# for i in range(1,15):
#     if i == 8:
#         break
#     else:
#         print(i)

# print("The loop is end")

# for i in range(1,15):
#     if i == 8:
#         continue
#     else:
#         print(i)

# print("The loop is end")


# for i in range(1,15):
#     if i == 8:              # Note: when break is execute then else will not execute and its inverse exists.
#         print("The break is executed:")
#         break
#     print(i)
# else:
#     print("the break is not executed")


# ---------------- Questions: -------------------------


# 1. Accept an integer and Print hello world n times
# n = int(input("Enter the number: "))
# for i in range(n):
#     print("Hello World!")
# --------------------------------------------------------

# 2. Print natural number up to n
# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     print(i)
# --------------------------------------------------------

# 3. Reverse for loop. Print n to 1
# n = int(input("ENter the number: "))
# for i in range(n,0,-1):
#     print(i)
# -----------------------------------------------------------

# 4. Take a number as input and print its table
# n = int(input("ENter the number: "))
# for i in range(n,(n*10)+1,n):
#     print(i)

# i is a loop variable (also called an iterator).
# It stores the current value produced by range() in each iteration of the loop.
# You can think of i as a temporary box that holds a new number each time the loop runs.

# 2nd method:
# n = int(input("ENter the number: "))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i} ")

# ------------------------------------------------------------------------------------------

# 5. Sum up to n terms
# n = int(input("Enter the number: "))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(sum)

# -------------------------------------------

# 6. Factorial of a number
# n = int(input("Enter the number: "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact*i
# print(fact)
# -----------------------------------------------

# 7. Print the sum of all even & odd numbers in a range separately

# n = int(input("Enter the number: "))
# even = 0
# odd = 0
# for i in range(1,n+1):
#     if(i%2 == 0):
#         even = even + i
#     else:
#         odd = odd + i
        
# print(f"Even and odd sum are {even} , {odd}")
# ------------------------------------------------------------

# 8. Print all the factors of a number
# n = int(input("Enter the number: "))
# for i in range(1,n,1):
#     if(n%i == 0):
#         print(i)
# ------------------------------------------------------------

# 9. Accept a number and check if it a perfect number or not.
# A number whose sum of factors is equal to the number itself
# Ex -  6 = 1, 2, 3 = 6

# n = int(input("Enter the number: "))
# sum = 0
# for i in range(1,n,1):
#     if(n%i == 0):
#         sum = sum + i
# print(sum)
# if(sum == n):
#     print("It is a perfect number")
# else:
#     print("It is not a perfect number")
# ---------------------------------------------------------------

# 10. Check wether the number is prime or not

# n = int(input("Enter the number: "))
# count = 0
# for i in range(1,n+1,1):
#     if(n%i == 0):
#         count = count +1
# if count == 2:
#     print("Prime Number")
# else:
#     print("Not prime number")
# -------------------------------------------------------

# 11. Reverse a string without using in build functions

# a = input("Enter the string: ")
# b = ""
# print(len(a))
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]

# print(b)

# -------------------------------------------------------

# 12. Check string is Pallindrome or not

# a = input("Enter the string: ")
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]

# if(b == a):
#     print("It is Palindrom")
# else:
#     print("It is not Palindrom")


# -----------------------------------------------------
# 13. 
# a = "jdhfkj6347!@3"
# char = 0
# dig = 0
# spchr = 0

# for i in a:
#     if(i.isdigit()):
#         dig = dig +1
#     elif(i.isalpha()):
#         char = char +1
#     else:
#         spchr = spchr +1
# print(f"Digits are {dig}\nalphabets are {char}\nSpchar are {spchr} ")
            
