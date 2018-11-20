from sys import argv

script, input_file = argv

# read the entire file
def print_all(f):
    print(f.read())

# rewind the line count, back to 0.
def rewind(f):
    f.seek(0)

# pick a line to read through
def print_a_line(line_count, f):
    print(line_count, f.readline())

# open input_file
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

# set current line to 1 and then read that line
# 1
current_line = 1
print_a_line(current_line, current_file)

# add 1 to the current line and read that line
# 2
current_line += 1
print_a_line(current_line, current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")

# 1
current_line = 1
print_a_line(current_line, current_file)

# add 1 to the current line and read that line
# 2
current_line += 1
print_a_line(current_line, current_file)

# add 1 to the current line and read that line
# 3
current_line += 1
print_a_line(current_line, current_file)

# current_line is set as the first argument of print_a_line which is line_count
