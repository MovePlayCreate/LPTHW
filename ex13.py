import math
from sys import argv
# read the WYSS section for how to run this
#script, first, second, third = argv

fourth = input("Input a variable: ") 
script, first, second, third, fourth = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your fourth variable is:", fourth)

def fifth_variable(var):
    print(f"Your fifth variable is: {var}")
    
fifth_variable("fifth")

reps = 21
half_that = math.floor(reps / 2)
print(half_that)
