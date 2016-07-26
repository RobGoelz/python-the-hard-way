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

# we could do these two on one line, how?
# opens the file represented by the from_file varaible
# which is the second command line argument above
# and assigns it to the in_file variable
in_file = open (from_file)
# reads the contents of the file stored in the in_file
# variable into a new variable called indata
indata = in_file.read()

# prints the string and uses the python format operator
# for decimals to call in the length of the indata
# variable into the string, using the len module
print "The input file is %d bytes long" % len(indata)

# prints the string and uses the python format operator
# for raw input (printable object representation) (%r)
# to call in the evaluation of the existence of a file
# using the exists command imported at the top of this
# script
print "Does the output file exist? %r" % exists(to_file)

# prints string
print "Ready, hit RETURN to continue, CTRL-C (^C) to abort."
# waits for input
raw_input()

# opens the file to_file for writing and assigns it to a
# new variable called out_file
out_file = open (to_file, 'w')
# writes the contents of the indata variable, which
# remember is the content of the from_file file above
# and then writes the data out to the out_file variable
# which is really the to_file file variable called above
out_file.write(indata)

# prints string
print "Alright, all done."

# closes all files
out_file.close()
in_file.close()
