# declares a variable that uses the python format operator for "printable representation of an object" (%r) 
# otherwise known as raw input and will accept in any four objects and display them (print) as a string
formatter = "%r %r %r %r"

print formatter % (1,2,3,4) # here it's passing the decimal numbers 1,2,3,4
print formatter % ("one","two","three","four") # here it's passing strings to the formatter variable
print formatter % (True,False,False,True) # here it's passing boolean values to the formatter variable
print formatter % (formatter,formatter,formatter,formatter) # this is fun - passing the variable back into the variable o.O
#  passing complex strings to the formatter variable, each separated by comma, newline and tab for style
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)

