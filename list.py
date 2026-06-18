# Data Structures:

# to store multiple values in a single variable , we use data structures.

# 4 main data structues are present: list , tuple , dictionary , set

#---------------------- List data structure ---------------------------------------

# Syntax of list is , we uses sqare brackets for this.

# a = [12,23,44,1,2]

# a = [12,23,44.5,True,printf()]        # Heterogeneous Nature

# a = [12,23,44.5,12,16,18,True,print()]   

# print(a[1])
# print(a[0:5])
# print(a[-1])
# print(a[-2])

#------------- traversing on Lists--------------

# 1st Way=> using Indexing
# a = [12,23,44,12,16,18.5] 

# for i in range(len(a)):
#     print(a[i])

# 2nd way = directly on values of list
# for i in a:
#     print(i)

#------------------- Methods of Lists--------------

# Mehtod = A method is a function that is defined in a class.

# print(dir(list))
# help(list)

# a = [12,23,44,12,16,18.5]


# a.append(7)             # Append object to the end of the list.     
# a.append(89)
# a.insert(2,4)             # insert(index,object)
# a.extend([2,6,8])           # add multiple elements at the end.
# a.count(12)
# print(a.count(12))
# a.sort()
# print(a)
# a.reverse()
# print(a)

# a[0] = 10       # Mutability , not occurs in strings.
# print(a)



# ----------------- Questions on Lists --------------------------------

# 1. Print positive and negative elements of an List.

# l = [1,-9,3,-4,5,-2]

# print("Positive Elements:")
# for i in l:
#     if i >=0:
#         print(i)
# print("Negative Elements:")
# for i in l:
#     if i <0:
#         print(i)


# 2. Mean of List elements

# a = [1,9,3,4,5,2]
# sum = 0

# for i in range(len(a)-1):
#     sum = sum + a[i]
    
# mean = sum/len(a)
# print(f"Mean = {mean}")


# 3. Find the greatest element and print its index too

# a = [1,9,3,4,5,12]
# max = a[0]
# index = 0
# for i in range(len(a)):
#     if a[i] > max:
#         max = a[i]
#         index = i
# print(f"Maximum element {max} at index {index}")


# 4. Find the second greatest element

# a = [1,9,3,4,5,2]

# max = a[0]
# index = 0
# for i in range(len(a)):
#     if a[i] > max:
#         max = a[i]
#         index = i

# pop = a.pop(index)
# smax = 0
# for i in range(len(a)-1):
#     if(a[i]>=smax):
#         smax = a[i]
#     else:
#         smax = smax

# print(smax)

# ------- 2nd method -----------------
# a = [1,9,3,4,5,2]

# max = a[0]
# sec_max = a[0]
# index1 = 0
# index2 = 0
# for i in range(len(a)):
#     if a[i] > max:
#         sec_max = max
#         max = a[i]
#         index1 = i
#     elif a[i]>sec_max:
#         sec_max = a[i]
#         index2 = i
# 
# print(f"Max value {max} is at index {index1}")
# print(f"Seconde max value {sec_max} is at index {index2}")
 
# 5. Check if List is sorted or not.

# a = [1,2,3,4,5,9]
# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("Not Sorted")
#         break
# else:
#     print("Sorted")
