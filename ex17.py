# import the argv (argument) variable from the sys module
from sys import argv

# import the exists command from the os.path module
from os.path import exists

# assign variables to positional command line arguments
# i.e. arguments from right to left get the varaibles:
# "script", "from_file", and "to_file"
script, from_file, to_file = argv

# print the string, taking in the string contents of 
# the variables "from_file" and "to_file" using the 
# python format operator for strings (%s)
print "Copying from %s to %s" % (from_file, to_file)

# opens the file represented by the from_file varaible
# which is the second command line argument above
# reads file using the pass (.) to the read() function
# and assigns it to the in_file variable
indata = open(from_file).read()

# prints the string and uses the python format operator
# for decimals to call in the length of the indata
# variable into the string, using the len module
print "The input file is %d bytes long" % len(indata)

# prints the string and uses the python format operator
# for raw input (printable object representation) (%r)
# to call in the evaluation of the existence of a file
# using the exists command imported at the top of this
# script, then returns "True" if file exists
# or "False" if the file does not exist
print "Does the output file exist? %r" % exists(to_file)

# prints string
print "Ready, hit RETURN to continue, CTRL-C (^C) to abort."
# waits for input
raw_input()

# opens the file to_file for writing and passes it (.)
# to write, and writes to the file using the data in 
# the indata variable from above
open (to_file, 'w').write(indata)

# prints string
print "Alright, all done."

