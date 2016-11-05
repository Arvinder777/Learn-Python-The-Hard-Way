from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# just prompt a question and wait for enter
input("?")
# open file with write mode
print("Opening the file...")
target = open(filename, 'w')
# erase content of the file
# but this isn't necessary if opened file with write mode. see pydoc open
#print("Truncating the file. Goodbye!")
#target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# always make sure to close the file
print("And finally, we close it")
target.close()

txt = open(filename)
print("Here is what you have wrote : ")
print(txt.read())