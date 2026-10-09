"""Beginner walkthrough of Python basics: variables, primitive types, and core data structures (list, dict, tuple, set)."""

# This script demonstrates basic Python programming concepts:
# - printing output
# - variables and primitive data types (string, float, int, bool)
# - checking data types with type()
# - collections such as lists, dictionaries, tuples, and sets
# - accessing dictionary values and printing results

print("Hello, World!")
# variables
name = "Sumeet"
years_of_experience = 12.5 # constant
no_of_environments = 3
is_working=True


# int, float, str, bool  - Primitives data types

print(type(no_of_environments))
print(type(years_of_experience))
print(type(name))
print(type(is_working))

# Data Structures in Python
# list, tuple, set, dict - Non primitive data types


environments = ["dev", "qa", "prod"] #list
print(type(environments))

info = {

"name" : "Sumeet",
"years_of_experience" : 12.5,
"env" : ["dev", "qa", "prod"], 

}
print(type(info))    # recognizes as dictionary
print(info["name"])  # dictionary access

#tuple
days_of_week = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
days_of_week[0] # Monday    


#set - It will have only unique values, no duplicates
num = {1, 2, 3, 4, 5, 6,1,2,3,4,5,6}
print(num)







