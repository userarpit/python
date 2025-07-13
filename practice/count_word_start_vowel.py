names = ['Arpit', 'ffgsd', 'ikkadf', 'onskdhiasdf', 'ukkjh']


def count(names):
    return sum(1 for i in names if i[0].lower() in ['a', 'e', 'i', 'o', 'u'])


print(count(names))
