# shall change to binary
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# 1. string is put inside a string
y = "Those who knows %s and those who %s." % (binary, do_not)

print(x)
print(y)

# %r is useful to print anything
# 2. string is put inside a string
print("I said: %r." % x)
# 3. string is put inside a string
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# 4. string is put inside a string
print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

# + here concatenates since both left and right are in string
print(w + e)
