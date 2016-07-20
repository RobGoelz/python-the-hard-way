# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun" # declares days as a string variable containing shortname for days of the week

# declares months as a string variable containing shortname for months of the year and appending a \n (newline)
# character at the end of each preceeding month
months = "\nJan\nFeb\nMar\nApr\nMay\nJune\nJul\nAug"

print "Here are the days: ", days # prints the string followed by the variable "days" declared above
print "Here are the months: ", months # prints the string followed by the variable "months" declared above

# prints a string of type multiple lines until the closure of the print with three double-quotes """
# also appears to respect the separation of lines without inclusion of the \n character as above (nice hack)
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
