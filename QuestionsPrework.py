# QUESTIONS:
# ==================Question 1====================
# Write a function to print "hello_USERNAME!" 
# USERNAME is the input of the function. 
# The first line of the code has been defined as below. 
#===================ANSWER======================== 
# def hello_name(user_name):
#     print("Hello" +" "+ user_name.title())
# hello_name("Jimbo")
# 
# 
# 
# ===============Question 2=======================
# # Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing 
# 
# ===============ANSWER===========================
# def first_odds():
#     for odd in range(1,101,2):
#         print(odd)
# first_odds()



#============== Question 3========================
# Please write a Python function,
#  max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below. 

# =============ANSWER=============================
# def max_num_in_list(a_list):
#     nums = max(a_list)
#     return nums

# print(max_num_in_list([2,35,8,5,23,9,67,54]))

#============== Question 4=========================
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, 
# unless it is also divisible by 400. The return should be boolean Type (true/false). 


# =============ANSWER==============================
# def is_leap_year(a_year):
#     if a_year %4 == 0 and (a_year %400 == 0 or a_year %100 != 0):
#         print(True)
#     else:
#         print(False)

# is_leap_year(2020)

# ==============Question 5===========================

# Write a function to check to see if all numbers in the list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type. 

def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i+1]:
            i += 1
        else:
            status = False
            break
    print(status)
is_consecutive([45,46,47,48,49])
