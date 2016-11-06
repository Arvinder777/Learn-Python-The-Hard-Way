# True
print(1, True and True)
# False
print(2, False and True)
# False
print(3, 1 == 1 and 2 == 1)
# True
print(4, "test" == "test")
# True
print(5, 1 == 1 or 2 != 1)
# True
print(6, True and 1 == 1)
# False
print(7, False and 0 != 0)
# True
print(8, True or 1 == 1)
# False
print(9, "test" == "testing")
# False
print(10, 1 != 0 and 2 == 1)
# True
print(11, "test" != "testing")
# False
print(12, "test" == 1)
# True
print(13, not (True and False))
# False
print(14, not (1 == 1 and 0 != 1))
# False
print(15, not (10 == 1 or 1000 == 1000))
# False
print(16, not (1 != 10 or 3 == 4))
# True
print(17, not ("testing" == "testing" and "Zed" == "Cool Guy"))
# True
print(18, 1 == 1 and (not ("testing" == 1 or 1 == 0)))
# False
print(19, "chunky" == "bacon" and (not (3 == 4 or 3 == 3)))
# False
print(20, 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))

# Python and many languages like to return one of the operands to their boolean expressions
# rather than just True or False. This means that if you did False and 1 you get the first
# operand (False) but if you do True and 1 your get the second (1). Play with this a bit.
print("test" and "test")
print(False and 1)
print(True and 1)
print("test" and "test1")
