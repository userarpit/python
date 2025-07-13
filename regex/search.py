from re import search

string = """I was born on June 24"""

match = search(r"([a-zA-Z]+)\s(\d+)",string) # match is a object here

    # So this will print "June 24"
print ("Full match: %s" % (match.group(0)))
 
    # So this will print "June"
print ("Month: %s" % (match.group(1)))
 
    # So this will print "24"
print ("Day: %s" % (match.group(2)))

print(match.re)
print(match.string)
print(match.start())
print(match.end())
print(match.span())