from sys import argv

script, user_name, user_lastname = argv
prompt = '$ '

print("Hi %s, I'm the %s script." % (user_name + " " + user_lastname, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % (user_name + " " + user_lastname))
likes = input(prompt)

print("Where do you live %s?" % (user_name + " " + user_lastname))
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
    Alight, so you said %r about liking me.
    You live in %r. Not sure where that is.
    And you have a %r computer. Nice
    """ % (likes, lives, computer))