# Conditions

# a = 15
# if a > 10:
#     print("Perform task A")
# else:
#     print("Perform task B")

# money = int(input("Enter amount: "))

# if money == 10:
#     print("Buy icecream.")
# else:
#     print("Buy chocolate.")



# elif: to check multiple conditions we use elif.

# money = int(input("Enter amount: "))

# if money == 10:
#     print("Buy icecream.")
# elif money == 20:
#     print("Buy chocolate")
# else:
#     print("Buy cone.")

# Multiple eilf can be used for checking multiple conditions.

# money = int(input("Enter amount: "))

# if money == 10:
#     print("Buy icecream.")
# elif money == 20:
#     print("Buy chocolate")
# elif money == 30:
#     print("Buy cake")
# elif money == 40:
#     print("Buy biscuit")
# else:
#     print("Buy nothing.")


# -----------------------------------------------------------------------

# Questions on Conditions

# 1. Accept two numbers and print the greatest between them.
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1 > num2 :
#     print(f"Greatest number is {num1}.")
# elif num2 > num1:
#     print(f"Greatest number is {num2}.")
# else:
#     print("Both numbers are same.")


# Q2. Accept the gender from the user as char and print the 
# respective greeting message 
# Ex - Good Morning Sir (on the basis of gender)

# gender = input("Enter gender M/F : ")
# if gender == "M" or gender == "m":
#     print("Good Morning Sir!")
# elif gender=="F" or gender =="f":
#     print("Good Morning Madam!")
# else:
#     print("Enter correct gender")

# Q3. Accept an integer and check whether it is an even number 
# or odd.

# num = int(input("Enter the number: "))
# if num%2 == 0:
#     print("Even Number")
# else:
#     print("Odd number")

# Q4. Accept name and age from the user. Check if the user is a 
# valid voter or not.
# Ex- “hello shery you are a valid voter”

# name = input("Enter name: ")
# age = int(input("Enter age: "))

# if age >= 18:
#     print(f"hello {name} you are a valid voter.")
# else:
#     print(f"hello {name} you are not a valid voter.")
#     print(f"You can vote after {18-age} years.")
    


# Q5. Accept a year and check if it a leap year or not (google to 
# find out what is a leap year)
    
# year = int(input("Enter year: "))

# if (year%100==0 and year%400==0):
#     print("It is a leap year.")
# elif year%4==0 and year%100!=0:
#     print("It is a leap year.")
# else:
#     print("It is normal year.")

# Q6
# If- elif ladder
# You can also create if elif ladder using multiple conditions of 
# elif.
# For understanding solve this question
# take the input of temperature in celsius
# Below 0°C → "Freezing Cold" 
# 0°C to 10°C → "Very Cold"
# 10°C to 20°C → "Cold" 
# 20°C to 30°C → "Pleasant" 
# 30°C to 40°C → "Hot" 
# Above 40°C → "Very Hot "

# temp = int(input("Enter temperature: "))

# if(temp<0):
#     print("Freezing Cold")
# elif (temp>=0 and temp<10):
#     print("Very Cold")
# elif (temp>=10 and temp<20):
#     print("Cold")
# elif (temp>=20 and temp<30):
#     print("Pleasant")
# elif (temp>=30 and temp<40):
#     print("Hot")
# else:
#     print("Very Hot")

