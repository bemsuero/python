from sys import argv
#read the WYSS section for how to run this.
# script, first, second, third = argv
#
# print("The script is called:", script)
# print("Your first variable is:", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)

# script, hair, eyes, height, weight = argv
#
# print("The script is called:", script)
# print("Your hair color is:", hair)
# print("Your eye color is:", eyes)
# print("Your height is:", height)
# print("Your weight is:", weight)

script, username, password = argv

print("The script is called:", script)
if username == "bemsuero":
    print("Welcome: ", username)
if password == "1234":
    activity = input("What would you like to do? ")
    print(activity)
