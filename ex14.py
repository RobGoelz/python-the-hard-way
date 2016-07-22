# import argv (argument variable) from sys module
from sys import argv

# assign varaibles passed from inital command line
# inputs from left to right
script, user_name = argv
# assign prompt variable to ">" to display a
# prompt-like format in our script
prompt = '> '

# calls the user name and script variables assigned
# from argv above and prints them
print "Hi %s, I'm the %s script." % (user_name, script)

print "I'd like to ask you a few questions."

# prints do you like me {user_name variable}?
# user_name assigned from argv
print "Do you like me, %s?" % user_name

# assigns a varaible to the user answer to the question
# Do you like me? uses raw_input to capture the answer
# and raw_input displays the prompt variable ">"
# to the user to emulate a prompt format for answer
likes = raw_input (prompt)

# prints string and user_name assigned from argv
print "Where do you live, %s?" %user_name

# assigns a varaible to the user answer to the question
# Where do you live? uses raw_input to capture the answer
# and raw_input displays the prompt variable ">"
# to the user to emulate a prompt format for answer
lives = raw_input (prompt)

print "What kind of computer do you have?"

# assigns a varaible to the user answer to the question
# What kind of computer do you have? 
# uses raw_input to capture the answer
# and raw_input displays the prompt variable ">"
# to the user to emulate a prompt format for answer
computer = raw_input (prompt)

# prints all of the content of the answers gathered above
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

