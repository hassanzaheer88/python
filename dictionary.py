# ---------------------- Dictionary / HashMap in C++ --------------------------------

# d = {}
# Empty set has type dictionary.
# print(type(d))          # Type = dictionary 

# d= {1,2,3}      # It will become set.

# So For Dictionary , we store values in Key Pair form.

# d = { 1:"hello" }       # 1 = key , hello = value , : s is used for assigning values.
# print(type(d))

# d = { 1:"hello" , 2:50 }

# Mutability: key cannot be change , but it can only be deleted, and value can be changed/

# Duplicates: Key must be unique , values can be duplicates.
# e.g:
# d = { 1:"hello" , 2:50 ,3:"hello"}

# Heterogeneous Nature
# e.g: 
# d = { 1:"hello" , 2:50 ,"hello":"hello"}


# e.g:
# d = { 10:100,20:200,30:300,40:400}

# Values will be accessed by its keys.
# print(d[0])         # Error: because there does not exist key = 0
# print(d[10])            # Ans: 100
# print(d[40])

# CRUD operations can only applied on Values and not on keys.

# d = { 10:100,20:200,30:300,40:400}

# d[10] = 1000      # updating:here updation occurs
# print(d)

# d.update({50:500})          # New key:value wil be inserted in dictionary.
# print(d)

# Another method insetead of using Update.

# d[50] = 500                 # Creation : here python wil create new key value in dictionary.
# print(d)                    #pyhton will not find key = 50 so it added new key vlaue.

# del d[30]           # for deleting
# print(d)

# --------------------- Dictionary Traversing ---------------------------------------

# We can traverse both keys and values in dictionary, but 
# default loop is set on keys and you can access the values 
# because of keys.

# d = { 10:100,20:200,30:300,40:400}

# for i in d:           # it will go on directly KEYS.
    # print(i)          # to access Keys
    # print(d[i])       # to access values

# Second method to acces directly Values.
# for i in d.values():
#     print(i)     


# ---------------- Dictionary Methods -------------------------------------

# help(dict)

# d = { 10:100,20:200,30:300,40:400}

# d.clear()           # removes all the keys and values.

# ------------------ Deep Copy Vs Shallow Copy ---------------------

# First apply on list
# a = [1,2,3,4]
# b = a
# b[0] = 100

# Ideally as we can see that we are changing only in list b but here 
# the list a will also be change . This is know as DEEP COPY. This occurs in dict also.
# print(a)        # Output: [100, 2, 3, 4]

# To prevent from DEEP COPY we uses a function that returns us a SHALLOW COPY.
# copy() function: always returns a SHALLOW COPY.

# a = [1,2,3,4]
# b = a.copy()
# b[0] = 122
# print(a)          # Output: [1, 2, 3, 4]
# ----------------------------------------------------------------------------------

# ---------------- Dictionary Methods -------------------------------------

# d = { 10:100,20:200,30:300,40:400}
# d2 = d.copy()
# d2[10] = 567
# print(d)        # {10: 100, 20: 200, 30: 300, 40: 400}
# print(d2)       # {10: 567, 20: 200, 30: 300, 40: 400}



# d = { 10:100,20:200,30:300,40:400}

# d2 = d.get(20)
# print(d2)           # Output: 200

# print(d.items())      # dict_items([(10, 100), (20, 200), (30, 300), (40, 400)])
# print(d.keys())         # dict_keys([10, 20, 30, 40])

# --------------- Questions --------------------------------

# 1. Write a Python script to merge two Python dictionaries

# d1= {1:10,2:20,3:30}
# d2= {4:40,5:50,6:60}

# d3 = d1 | d2
# print(d1)

# d1.update(d2)             #Another method

# --------- Another methode ---------
# for i in d2:
#     d1[i] = d2[i]           # Creating : new key values will inserted in d1    .

# print(d1)

# 2. Write a Python program to sum all the values in a dictionary

# d1 = {1:10,2:20,3:30}
# sum = 0

# for i in d1:
#     sum = sum + d1[i]

# print(sum)

# -------- Another method--------
# for i in d1.values():
#     sum = sum + i

# print(f"Sum of values is {sum}")

# 3. Count the frequency of each element in a list

# a = [1,2,3,4,1,2,3,4,5,2,1,1,2,3,4]
# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1
 
# print(d)


# 4. Write a Python program to combine two dictionary by adding 
# values for common keys.


# d1= {1:10,2:20,4:30}
# d2= {4:40,5:50,6:60}

# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]  

# print(d1)
