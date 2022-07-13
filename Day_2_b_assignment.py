# Author: Elliott Larsen
# Date: 7/12/2022
# Description: Day 2-b assignment.

#------------------------------------------------------------------------------------------------
# 1. Create a list with one number, one word and one float value. Display the output of the list.
#------------------------------------------------------------------------------------------------
lst_1 = [1, "Hello", 3.14]
print(lst_1)
#output: [1, 'Hello', 3.14]

#-------------------------------------------------------------------------------
# 2. I have a nested list [1,1,[1,2]], how to grab the value of 2 from the list.
#-------------------------------------------------------------------------------
lst_2 = [1,1,[1,2]]
print(lst_2[2][1])
# output: 2

#-----------------------------------------------------
# 3. lst=['a','b','c'] What is the result of lst[1:]?
#-----------------------------------------------------
# it would be ['b', 'c']
# lst=['a','b','c']
# print(lst[1:])

#-------------------------------------------------------------------------------------------------------------------
# 4. Create a dictionary with weekdays an keys and week index numbers as values. do assign dictionary to a variable.
#-------------------------------------------------------------------------------------------------------------------
week_dict = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4}

#----------------------------------------------------
# 5. D={‘k1’:[1,2,3]} what is the output of d[k1][1].
#----------------------------------------------------
# it would be 2
# D={'k1':[1,2,3]}
# D['k1'][1]

#-------------------------------------------------
# 6. Can you create a list [1,[2,3]] into a tuple.
#-------------------------------------------------
lst_3 = [1,[2,3]]
a, b = lst_3[0], lst_3[1]
temp_lst = []
temp_lst.append(a)
for i in b:
    temp_lst.append(i)
return_tup = tuple(temp_lst)
print(return_tup)

#----------------------------------------------------------------------------------------------
# 7. With a single set function can you turn the word ‘Mississippi’ to distinct character word.
#----------------------------------------------------------------------------------------------
temp_set = set("Mississippi")

#--------------------------------------------------------
# 8. Can you add an element ‘X’ to the above created set.
#--------------------------------------------------------
temp_set.add("X")

#----------------------------
# 9. Output of set([1,1,2,3])
#----------------------------
print(set([1,1,2,3]))

#---------------------------------------------------------------------------------------------------------------------------------------------
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,between 2000 and 3200 (both included).
#---------------------------------------------------------------------------------------------------------------------------------------------
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end = ', ')

#--------------------------------------------------------------------
# Write a program which can compute the factorial of a given numbers.
#--------------------------------------------------------------------
def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x - 1)

x = int(input("Please enter a number: "))
print(factorial(x))


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def square_num(x):
    return_dict = dict()

    for i in range(1, x + 1):
        return_dict[i] = i ** 2
    
    return return_dict

x = int(input("Please enter a number: "))
print(square_num(x))