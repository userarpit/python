a = ['mmlknlksd klansdfjadf','alsdhfoiha jasodifoiads']

with open("test1.txt","w") as file:
    for sentence in a:
        file.write(sentence)
        file.write("\n")