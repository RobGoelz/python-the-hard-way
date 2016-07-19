# Sets variable x to string value and calls python format operator for integer decimal (%d) to receive value "10" into the string
x = "There are %d types of people." % 10

# sets variable binary to string "binary"
binary = "binary"

# sets variable do_not to string "don't"
do_not = "don't"

# sets variable y to string value that calls python format operator for string (%s) to receive variable values for strings "binary" 
# and "do_not" into the y variable - in other words, nested string variable calls into a new variable (cool!)
y = "Those who know %s and those who %s." % (binary, do_not) # <- string inside a string x 2

# prints variable x
print x
# prints variable y
print y

# prints a new string and uses the python format operator for "printable representation of an object" (%r) to receive the value of
# variable x into the string - in other words, another way of "nesting" a string variable without declaring a new variable

print "I said: %r." % x # <- string inside a string

# prints a new string and uses the python format operator for string (%s) to receive the value of variable y into the string
# this is yet another way to "nest" a string variable into a new string, but here without calling a new string from a variable
# note the %s here instead of the %r - string verses representation - %r should be thoughit of as "raw" & used for debugging

print "I also said: '%s'." % y # <- string inside a string

# sets variable hilarious to boolean value "False"
hilarious = False

# sets variable joke_evaluation to a string value that calls the python format operator for "printable representation of an object"
# (%r) to receive the value of any object
joke_evaluation = "Isn't that joke so funny?! %r"

# prints the string values in variable joke_evaluation and passes the variable hilarious to the %r in the joke_evaluation variable
# which, in turn, prints out the "printable representation" of the hilarious object, in this case the boolean value False
print joke_evaluation % hilarious

# sets variable w to string
w = "This is the left side of..."
# sets variable e to string
e = "a string with a right side."

# prints concatenated string consisting of the contents of both variables - in other words, both strings back to back to create a 
# new sentence
print w + e
