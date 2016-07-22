# takes raw_input from the prompt contained in 
# parenthesis () and assigns it to variable "age"
age = raw_input("How old are you? ")
# takes raw_input from the prompt contained in 
# parenthesis () and assigns it to variable "height"
height = raw_input("How tall are you? ")
# takes raw_input from the prompt contained in 
# parenthesis () and assigns it to variable "weight"
weight = raw_input("How much do you weigh? ")

# prints string and uses python format operator %r to read raw input from
# variables called in the string and print them as printable representations
# of the variable objects (so that you don't have to know the variable type)
print "So you're %r old, %r tall, and %r heavy." % (
	age, height, weight) # <- NOTE :formatting here for cleaner reading
