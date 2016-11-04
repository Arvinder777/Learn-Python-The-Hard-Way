# in python 2, you put comma instead to make it not to add new line
# e.g. print "How old are you?",
print("How old are you?", end=" "),
age = input()
# following also works
# e.g. age = input("How old are you? ")

print("How tall are you?", end=" "),
height = input()
print("How much do you weigh?", end=" "),
weight = input()

print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))

#work = input("Where do you work? ")
#print("So you work for %s." % work)

# x = int(input("Enter a number: "))
# y = int(input("Enter a second number: "))
# print('The sum of ', x, ' and ', y, ' is ', x+y, '.', sep='')