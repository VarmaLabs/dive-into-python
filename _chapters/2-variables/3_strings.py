name = "Ram"
with_quote = "I have a ' quote in me"
multiline_string = """I have multiple lines in me.
I have multiple lines in me.
I have multiple lines in me.
"""

# Escaping String
print "I said, I\'am driving."

# String Formating

# C like
"%s %s" %('hello', 'world')
# => 'hello world'

# PEP 3010 style
"{0} {1}".format('hello', 'world')
# => 'hello world'

