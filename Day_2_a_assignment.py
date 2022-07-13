# Author: Elliott Larsen
# Date: 7/12/2022
# Description: Day 2-a assignment.


#----------------------------------------------------------------------------------------------------------------
# 1.Write a string that returns just the letter ‘r’ from ‘Hello World’ For example, ‘Hello World’[0] returns ‘H’.
# You should write one line of code. Don’t assign a variable name to the string.
#----------------------------------------------------------------------------------------------------------------
print("Hello World"[8])
# output: r

#------------------------------------------------------------------------------------------------------
# 2. String slicing to grab the word ‘ink’ from the word  ‘thinker’ S=’hello’,what is the output of h[1]
# S=’hello’,what is the output of h[1]
#------------------------------------------------------------------------------------------------------
print("thinker"[2:5])
# output: ink

S = "hello"
print(h[1])
# output:   
# File "/Users/name/Desktop/SmoothStack/Assignments/Day_2_a_assignment.py", line 21, in <module>
#    print(h[1])
#NameError: name 'h' is not defined

#------------------------------------------
# 3. S=’Sammy’ what is the output of s[2:]”
#------------------------------------------

# It would be "mmy"
#s = "Sammy"
#print(s[2:])

#----------------------------------------------------------------------------------------------
# 4. With a single set function can you turn the word ‘Mississippi’ to distinct character word.
#----------------------------------------------------------------------------------------------
print(set("Mississippi"))

#---------------------------------------------------------------------------------------------------------------
#  5. The word or whole phrase which has the same sequence of letters in both directions is called a palindrome.
#  Your goal in this programming exercise is to determine, whether the phrase represents a palindrome or not.
#---------------------------------------------------------------------------------------------------------------

def is_pal(string):
    string_arr = []
    for i in string:
        if i.isalnum():
            string_arr.append(i.lower())
        else:
            continue
    
    return string_arr[::] == string_arr[::-1]