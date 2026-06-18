
#---------------------- Tuple data structure ---------------------------------------

# a = (2,3,4,5,6)

# print(type(a))     # Type: Tuple 
#a[1] = 12            # tuples are not mutable , means you cannot change the value.
#print(a)             # Error: tuple' object does not support item assignment.

# b = (2,3,46,7,7,7)                    # Duplication is possible
# b = (2,3,46,7,5.6,print(),True)         # Heterogeneous nature

# Traversing is same as list , strings.
# 1. using index        2.direct access
# a = (2,3,4,5,6)

# for i in a:
#     print(i)
    
# for i in range(len(a)):
#     print(a[i])

#-------------- Methods for Tuple ----------------------

# Only 2 methods exist for Tuple

# a = (2,3,4,5,6,5,65)
# index = a.index(5)
# print(index)

# count = a.count(5)
# print(count)


#----------------- Main Feature is: Tuple Unpacking ----------------

# a = (1,2,3,4)

a,b,c,d = (1,2,3,4)   # Tuple unpacking = assigning multiple variables multiple values.
# print(a)
# print(b)

# a =(1)
# print(type(a))      # Type = int because it has unpack, only single variable and single 
                    # value is assign to that variable that's why it shows integer type

# To not Unpack we will do this
# a = (a,)
# print(type(a))      # type = tuple

# -----------------------------------------------------------------------------------------------

# --------------------- Set ---------------------------------------------

# a = {}                  # Not empty set , It is dictionary.

# a = {2,3,4,5,6}         # always provide values in braces to make a Set.

# a[0] = 12

# a = {2,3,4,5,6,6,4}     # Should contain uniques values.
# print(a)                 # Output: {2, 3, 4, 5, 6}


# Sets are Unordered. 
# a = {2,3,4,5,6,6,4}
# print(a[0])             # Error: 'set' object is not subscriptable

# Sets are Semi-Heterogeneou: Only some values like string, numbers, tuples.

# a = {2,3,4,5,6,6.5,"Hassan"} 

# a = hash(12)
# print(a)          # does not hash the int value, it will shown as it is.
# b= hash("Hassan")
# print(b)                # Sets uses hashing to store anything so Every time the hash 
# value is changes,so it does not maintains any order and hence sets are unordered.

# ----------------- Set Traversing -----------------------------------------------------
# a = {1,2,3,4}
# We cannot traverse using the index values because set does not have any order.

# for i in range(len(a)):
#     print(a[i])             # Error: 'set' object is not subscriptable

# Only the below method is possible but it will show elements randomly.

# for i in a:
#     print(i)
    
    
# b = {1,8,9,7,2,3,4}
    
# for i in b:
#     print(i)            # output: 1234789

# c = {1,8,9,7,"Hassan",2,3,4}
# for i in c:
#     print(i)            # It will show "Hassan" at any random position.It is 
                        # based on system's memory how he deals with hashing.
                        # e.g 1) at last 2)at last 3)at middle .

            
# ----------------- Set Methods -----------------------------------------------------

# Set methods give us Mutability(means we can change the values).

# a = {2,3,4,5}
# a.add(6)
# print(a)
# a.remove(2)         # a.discard() = a.remove() -> both are same.
# print(a)

# pop() method = pops the element randomly because hashing does not have any order.

# a = {2,3,4,5}
# a.pop()
# print(a)        # Output: it poped (2) randomly.


# a = {2,3,4,5}
# a.clear()       # remove all the elements.
# print(a)        # output: only shows set()

# ------------------ Special Methods ---------------------------------------------

# Set Operations

# a = {1,2,3,4,5}
# b = {4,5,6,7,8,}

# s = a.union(b)
# s =  a | b          # shortcut
# print(s)

# b = a.intersection(b)
# b = a & b               # shortcut
# print(b)


# c = a.difference(b)
# c = a - b               # shortcut
# d = b.difference(a)
# d = b - a               # shortcut

# print(c)
# print(d)

# Symmetric Difference

# f = a.symmetric_difference(b)
# f  = a ^ b                    #shortcut
# print(f)

#---------- Compound Operations------------

a = {1,2,3,4,5}
b = {4,5,6,7,8,}

b -= a
print(b)