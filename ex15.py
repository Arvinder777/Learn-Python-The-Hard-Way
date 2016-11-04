# import argv class from sys module
from sys import argv
# unpack arguments to variables
script, filename = argv
# open file and save the file object to txt
txt = open(filename)
# print content of stream
print("Here's your file %r:" % filename)
print(txt.read())

txt.close()

# input filename again
print("Type the filename again:")
file_again = input("> ")
# open file and save the file object to txt_again
txt_again = open(file_again)
# print content of stream
print(txt_again.read())

txt_again.close()