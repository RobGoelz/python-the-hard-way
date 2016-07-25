# calls the argv (argument) variable from the python sys module
from sys import argv

# assigns the variables script and filename to the first two
# arguments from the command line
script, filename = argv

# prints string and uses raw input format operator to print the
# contents of the filename variable
print "We're going to erase %r." % filename

# prints two strings giving the script user control of
# the script's progression:
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that hit RETURN."

# in essence, inserts a pause here for user input (Ctrl-C or Return)
raw_input ("?")

# prints string
print "Opening the file..."
# opens the file and assigns it to the variable target
target = open (filename, 'w')

# prints string
print "Truncating the file.  Goodbye!"
# truncates (clears) the file
target.truncate()

# prints string
print "Now I'm going to ask you for three lines."

# takes raw_input and assigns it to varaible line1
line1 = raw_input ("line 1: ")
# takes raw_input and assigns it to varaible line2
line2 = raw_input ("line 2: ")
# takes raw_input and assigns it to varaible line3
line3 = raw_input ("line 3: ")
# assigns all lines to one variable with end lines
all_lines = "%s\n%s\n%s\n" % (line1, line2, line3)

# prints string
print "I'm going to write these to the file"

# writes line1 variable out to the file
target.write(all_lines)

# prints string
print "And finally, we close the file."
# closes file with new content
target.close()
