''''
from collections import Counter

str1 = "Arpit Khandelwal"

WC = Counter(str1)
print(WC)

for letter,counter in WC.items():
    if counter > 1:
        print("{} is present {} times".format(letter,counter))
'''
def find_dup_char(input):
	x = filter(lambda x: input.count(x) >= 2, input)
	print(' '.join(set(x)))

# Driver Code
if __name__ == "__main__":
	input = 'geeksforgeeks'
	find_dup_char(input)