# imports "argument variable" (arg) from python "sys" module
# the sys module provides access to some objects used or 
# maintained by the python interpreter
from sys import argv

# below we see the purpose of the arg variable, which is to
# hold the arguments you pass to a python script when you
# run the python script
# here we're passing four arguments to the agrv variable
script, first, second, third = argv

# prints the "script" argument
print "The script is called:", script
# prints the "first" argument
print "The first variable is:", first
# prints the "second" argument
print "The second variable is:," second
# prints the "third" argument
print "The third varaible is:," third
