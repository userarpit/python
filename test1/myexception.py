class Sample(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return "str {}".format(self.value) 

    def __repr__(self):
        return "repr {}".format(self.value)

try:
    raise(Sample(10))
except Sample as s:
    print([s])



# NetworkError has base RuntimeError
# and not Exception
class Networkerror(RuntimeError):
	def __init__(self, arg):
		self.args = arg

try:
	raise Networkerror("Error")

except Networkerror as e:
	print(e.args)
