from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, "w")

print("trashing the file. Goodbye!")
# if you open the file with "w" then you don't need the next line.
# target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
# shorter way to write it.
target.write(f"""{line1}
{line2}
{line3}
""")


print("And finally, we close it then read it's new contents.")
target.close()
# need to do this if you open the file with "w" as it does not allow to read.
target = open(filename)

print(target.read())
