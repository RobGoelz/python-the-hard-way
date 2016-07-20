print "How old are you?", # prints string
age = raw_input  () # accepts input and places it into variable "age"
print "How tall are you?", # prints string
height = raw_input () # accepts input and places it into variable "height"
print "How much do you weigh?", # prints string
weight = raw_input () # accepts input and places it into variable "weight"

# prints string and uses python format operator %r to read raw input from
# variables called in the string and print them as printable representations
# of the variable objects (so that you don't have to know the variable type)
print "So, you're %r old, %r tall, and %r heavy." % (age, height, weight)

# NOTE : there is no conditional checks here for numerical values so these raw inputs will accept any input
