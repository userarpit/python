from re import split
from re import IGNORECASE

string1 = "On 12th Jan 2016, at 11:02 AM"
# '\W+' denotes Non-Alphanumeric Characters
# or group of characters Upon finding ','
# or whitespace ' ', the split(), splits the
# string from that point
print(split('\W+', 'Words, words , Words'))
print(split('\W+', "Word's words Words"))

# Here ':', ' ' ,',' are not AlphaNumeric thus,
# the point where splitting occurs
print(split('\W+', string1))

# '\d+' denotes Numeric Characters or group of
# characters Splitting occurs at '12', '2016',
# '11', '02' only
print(split('\d+', string1))


print("******")

# Splitting will occurs only once, at
# '12', returned list will have length 2
print(split('\d+', string1, 1))

# 'Boy' and 'boy' will be treated same when
# flags = re.IGNORECASE
print(split('[a-f]+', 'Aey, Boy oh boy, come here', flags=IGNORECASE))
print(split('[a-f]+', 'Aey, Boy oh boy, come here'))