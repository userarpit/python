import re

class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter._JustCounter__secretCount)

print(re.findall('[0-9]*', '12345678910'))
print(re.findall('[0-9]*?', '12345678910'))

print(re.findall('[0-9]{2,5}', '12345678910'))
print(re.findall('[0-9]{2,5}?', '12345678910'))