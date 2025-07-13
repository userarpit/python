from fact import fact
def count_words(string):
    return sum(1 for i in string.split(" "))


print(count_words("lakdliad alkdiad lakdfl kajsdf"))
print(fact(4))