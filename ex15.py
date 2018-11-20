# imports argv from the python library
from sys import argv

# # gives the arguments that we'll be using.
# script, filename = argv
#
# # sets txt to the file with file name filename
# txt = open(filename)
#
# # prints message
# print(f"Here's your file {filename}:")
#
# # opens and reads the file in txt
# print(txt.read())
# filename.close()

script = argv
# prints message
print("Type the filename again: ")

# sets file_again to file name
file_again = input("> ")

# opens file_again and sets it to txt_again
txt_again = open(file_again)

# reads txt_again
print(txt_again.read())
txt_again.close()
