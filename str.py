# Strings with newlines

# Multiline strings
multi_line = """This is a multiline string 
that spans multiple lines"""

m = 'This is a string\n spans multiple \n lines'
print(multi_line, m)

# Escape sequences
tabs = "This is a \" in a string."  # Incoporating tabs
quote = 'This is a \' in a string'  # Use quote characters within strings
print(tabs, quote)
raw_string = r'C:\Users\Allan\Documents\Tutor'
print(raw_string)

# Sequence Types(supports common operations for querying sequences)
name = "parrot"
print(name[4])

# String Methods

c = "name"
c_upper = c.capitalize()
print(c_upper)