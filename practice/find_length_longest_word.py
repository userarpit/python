string = 'the quicka brown foxaaaaa jumps over the lazy dog'


def find_longest_word(string):
    """find longest word

    Args:
        string (String): contain string in which longest word need to be find
    """
    list_string = string.split(' ')
    # for i, value in enumerate(list_string):
    #     # print(i, value)
    #     if i < len(list_string) - 1:
    #         if len(value) > len(list_string[i+1]):
    #             list_string[i], list_string[i +
    #                                         1] = list_string[i+1], list_string[i]
    # return list_string[-1]
    return max(list_string,key=len)
    


print(find_longest_word(string))
