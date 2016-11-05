from sys import argv

script, input_file = argv

# read the file
def print_all(f):
    print(f.read())

# file reader to point first again
def rewind(f):
    f.seek(0)

# first print linenumber and read line
def print_a_line(line_count, f):
    # without end='', double \n will be entered. As readline() adds one, and print() adds one.
    print(line_count, f.readline(), end='')

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)