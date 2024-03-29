import re
import sys


# Our regex line of code
pat = '\(?(\d{3})[-\)]?\s?(\d{3})[-\s]?(\d{4})$'
# Compile the string into an regex command 
repat = re.compile(pat)
# The mobile number to test on - provided as a user input
mob_no = sys.argv[1]

# Search our input with the regex code
search = repat.search(mob_no)

if search:
    # Print the three sets of numbers found
    print(f"""
    Area code - {search.groups()[0]}
    Exchange Code - {search.groups()[1]}
    Line extension - {search.groups()[2]}""")
else:
    # Print not found if the search failed
    print('Not Found')


