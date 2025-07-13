mylist = [1,3,65,2,4,6]

odd = filter(lambda a : a % 2 != 0, mylist)

for i in odd:
    print(i)
words = ["apple","banana","cherry","date","elderberry"]
filtered_words = filter(lambda x : len(x) > 5, words)
print(list(filtered_words))    
