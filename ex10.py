# declares variable tabby_cat and uses the escape character for tab (\t) at the beginning of the
# variable string so that the string will be indented (tabbed).
tabby_cat = "\tI'm tabbed in."

# declares variable persian_cat and uses the escape character for newline (\n) in the middle of the
# variable string so that the string gets split between two lines
persian_cat = "I'm split\non a line"

# declares variable backslash_cat and uses the escape character to print backslashes in the string
# when the string is printed
backslash_cat = "I'm \\ a \\ cat."

# declares variable fat_cat and uses the tripe-double-quote trick to have the variable contain
# multiple string lines and also calls tab (\t) and newline (\n) escape characters inside
# of the variable to create a complex string variable and a "tabbed" list
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
