# Loops

# Range -> range(s,s,s) -> (start,stop,steps)
# range(1,20,2)

# For loop

# a = range(1,21,1)
# for i in a:
#     print(i)

# i is a loop variable (also called an iterator).
# It stores the current value produced by range() in each iteration of the loop.
# You can think of i as a temporary box that holds a new number each time the loop runs.

# for i in range(1,21,1):
#     print(i)

# Note: in range(st,stop,step) -> start =0 =default , steps = 1 = default , stop = should be provide.

# for i in range(21):         #Ans will start from 0 bcz start = default = 0
#     print(i)

# for i in range(20,51):
#     print(i)

# for i in range(16,0,-1):
#     print(i)

# for i in range(-3,-16,-1):
#     print(i)

# Print a table of 5

# for i in range(1,11,1):
#     print(f"5 * {i} = {5*i}")

# for i in range(5,51,5):
#     print(i)

# n = int(input("Enter the Table number: "))
# for i in range(n,n*10+1,n):
#     print(i)

# Iterate over the Strings
# two types 1. using index , 2. directly over the string

# 1.
# a = "Hassan"
# for i in range(6):    #start = default = 0
#     print(a[i])

# a = "Hassan teaches computer science"
# print(len(a))
# for i in range(len(a)):
#     print(a[i])

# 2. 
# a = "Hassan"
# for i in a:
#     print(i)

# break vs continue vs else

# for i in range(1,21):
#     if i == 15:
#         break
#     print(i)

# for i in range(1,21):
#     if i == 15:
#         continue
#     print(i)


# for i in range(1,21):
#     if i == 15:
#         print("Break statement executed.")
#         break
#     print(i)
# else:
#     print("Else statement executed.")

# if break runs then else will not run and 
# if break dosn't not run then else will run.
    
# Questions on For Loop

# 1. Accept an integer and Print hello world n times

# n = int(input("Enter the number: "))
# for i in range(n):
#     print("Hello world")


# 2. Print natural number up to n
# n = int(input("Enter the number: "))
# for i in range(1,n+1):
#     print(i)

# 3. Reverse for loop. Print n to 1
# n = int(input("Enter the number: "))
# for i in range(n,0,-1):
#     print(i)


# 4. Take a number as input and print its table
# n = int(input("Enter the number for table: "))
# for i in range(n,n*10+1,n):
#     print(i)

# 2nd method
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")


# 5. Sum up to n terms
# n = int(input("Enter the number: "))
# sum = 0
# for i in range(1,n+1,1):
#     sum += i
# print("Sum = ",sum)

# 6. Factorial of a number

# n = int(input("Enter the number: "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print("Factorial = ",fact)


# 7. Print the sum of all even & odd numbers in a range separately
# n = int(input("Enter the number: "))
# evenSum = 0
# oddSum = 0
# for i in range(0,n+1,1):
#     if i%2 == 0:
#         evenSum = evenSum + i
#     else:
#         oddSum = oddSum + i
# print("EvensSum: ",evenSum)
# print("OddSum: ",oddSum)

# 8. Print all the factors of a number
# n = int(input("Enter the number: "))
# for i in range(1,n+1,1):
#     if(n%i) == 0:
#         print("Factor: ", i)

# 9. Accept a number and check if it a perfect number or not. 
# A number whose sum of factors is equal to the number itself 
# Ex -  6 = 1, 2, 3 = 
# n = int(input("Enter the number: "))
# sum = 0
# for i in range(1,n,1):
#     if(n%i) == 0:
#         sum = sum + i

# if sum == n :
#     print("perfect Number:",sum)
# else:
#     print("Not a perfect number",sum)

# 10. Check wether the number is prime or not
# n = int(input("Enter the number: "))
# count = 0
# for i in range(1,n+1):
#     if(n%i)==0:
#         count = count + 1
# if count == 2:
#     print("Prime Number")
# else:
#     print("Not a Prime Number")

# 11. Reverse a string without using in build functions.

# print(a[::-1])

# another methode
# n = input("Enter the string: ")
# str = ""
# for i in range(len(n)-1,-1,-1):
#     str = str + n[i]
# print("Reversed String: ",str)


# 12. Check string is Pallindrome or not

# e.g : palindrome = ababa
# n = input("Enter the string for Palindrome: ")
# str = ""
# for i in range(len(n)-1,-1,-1):
#     str = str + n[i]

# if str == n:
#     print("It is palindrome")
# else:
#     print("Not a palindrome")

# 13. Count all letters, digits, and special symbols from a given string 
# Given: str1 = "P@#yn26at^&i5ve" 
# Expected Outcome: 
# Total counts of chars, digits, and symbols 
# Chars = 8 
# Digits = 3 
# Symbol = 4

# n = input("Enter the string: ")
# chr = 0
# dig = 0
# sym = 0
# for i in range(len(n)):
#     if n[i].isalpha():
#         chr += 1
#     elif n[i].isdigit():
#         dig += 1
#     else:
#         sym += 1

# print(f"There are characters {chr} and digits {dig} and symbols {sym} ")

# -------------------------------------------------------------------------------
# While loop

# a = 1
# while a<=30:
#     print(a)
#     a = a + 1

# Questions on While Loop

# 1. Separate each digit of a number and print it on the new line

# 256 = 2, 5, 6 should print separately
# n = int(input("Enter any number: "))
# while n>0:
#     print(n % 10)
#     n = n // 10

# 2.Accept a number and print its reverse
# n = int(input("Enter any number: "))
# rev = 0
# while n>0:
#     rev = rev *10 + n % 10
#     n = n // 10
# print(rev)

# 3. Accept a number and check if it is a pallindromic number (If 
# number and its reverse are equal

# n = int(input("Enter any number: "))
# copy = n
# rev = 0
# while n>0:
#     rev = rev *10 + n % 10
#     n = n // 10         # n will be destroyed,its value will become 0.
# if rev == copy:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# 4. Create a random number guessing game with python

# import random
# num = random.randint(1,10)
# # print(num)
# count = 0
# while True:
#     guess = int(input("Enter the number: "))
#     if num == guess:
#         count = count + 1
#         print(f"You win in {count} tries.")
#         break
#     elif num < guess:
#         print("Go a little below")
#         count = count + 1
        
#     elif num > guess:
#         print("Go a little above")
#         count = count + 1
        
#     else:
#         count = count + 1
#         print("You lose And try again")