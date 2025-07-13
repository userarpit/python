string = 'the quick brown fox jumps over the lazy dog'

vowel_list = ['a', 'e', 'i', 'o', 'u']

def remove_vowel(string):
    withoutvowellist = [i for i in string if i.lower() not in vowel_list]
    return "".join(withoutvowellist)

print(remove_vowel(string))
