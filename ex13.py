# imports "argument variable" (arg) from python "sys" module
# the sys module provides access to some objects used or 
# maintained by the python interpreter
from sys import argv

# below we see the purpose of the arg variable, which is to
# hold the arguments you pass to a python script when you
# run the python script

# here we're essentially unpacking the arguments held in 
# argv and passing the contents to four varaibles, in order,
# from left to right:
script, first, second, third = argv

# prints the "script" variable assigned from argv
print "The script is called:", script
# prints the "first" variable assigned from argv
print "The first variable is:", first
# prints the "second" variable assigned from argv
print "The second variable is:," second
# prints the "third" variable assigned from argv
print "The third varaible is:," third
