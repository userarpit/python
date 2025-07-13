# Driver code
string = 'the quick brown fox jumps over the lazy dog'

print(sum(1 for i in set(string) if 96 < ord(i) <= 122) == 26)
