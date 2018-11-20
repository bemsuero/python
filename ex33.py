from sys import argv

# while loop
script, limit, addition = argv

i = 0
numbers = []

while i < int(limit):
    print(f"At the top i is {i}")
    numbers.append(i)

    i += int(addition)
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

# for loop
# script, limit = argv
#
# i = 0
# numbers = []
#
# for i in range(0, int(limit)):
#     print(f"At the top i is {i}")
#     numbers.append(i)
#
#     # i += int(addition)
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")
#
# print("The numbers: ")
#
# for num in numbers:
#     print(num)
