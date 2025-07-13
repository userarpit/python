vowel_list = ['a', 'e', 'i', 'o', 'u']


def count_vowel(string1):
    return sum(1 for i in string1 if i.lower() in vowel_list)


string1 = 'the quick brown fox jumps over the lazy dog'
print(f"Total Vowel {count_vowel(string1)}")
print(f"Total Vowel {count_vowel('Arpit')}")
