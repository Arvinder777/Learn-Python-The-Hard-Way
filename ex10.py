tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

raw_cat1 = "\'single quote\'"
raw_cat2 =  '\"double quote\"'
print('Print in raw = %r %r' % (raw_cat1, raw_cat2))
print('Print in pretty format = %s %s' % (raw_cat1, raw_cat2))
