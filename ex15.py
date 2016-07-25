# calls the argv (argument) variable from the python sys module
from sys import argv

# assigns the initial command line input
script, filename = argv

# opens the file using the filename variable provided by the
# initial command line argument (though argv)
# and assigns the contents of the file to the variable "txt"
txt = open (filename)

# prints the string & raw output of the filename varaible
print "Here's your file %r:" % filename
# prints the contents of the text variable by passing it to 
# the read function "read()"
print txt.read()
# closes file
txt.close()

# prints string to prompt for filename
print "Type the filename again:"

# takes in a filename from the command prompt using raw_input
# and the "> " characters to represent a prompt and assigns
# the file to a variable called file_again
file_again = raw_input("> ")

# opens the file specified by the file_again varaible
# assigns the contents of the file to the txt_again varaible
txt_again = open(file_again)

# prints the contents of the txt_again variable by passing it 
# to the read function "read()"
print txt_again.read()
# closes file
txt_again.close()
