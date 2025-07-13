import json
import jmespath
from difflib import get_close_matches

with open("practice/words.json","r") as file:
    load_file = json.load(file)

# print(load_file)
word_to_search = input("Enter word to search - ")

search_data = jmespath.search("".join(word_to_search).lower(),load_file)
if search_data:
    print(search_data)
else:
    search_data = jmespath.search(word_to_search.title(),load_file)
    if search_data:
        print(search_data)
    else:
        search_data = jmespath.search(word_to_search.upper(),load_file)
        if search_data:
            print(search_data)
        else:
            close_match = get_close_matches(word_to_search,load_file.keys(),n=1)
            if len(close_match) > 0:
                print(f"did you mean '{"".join(close_match)}' instead of {word_to_search}")
                decision = input("type y to continue - ")
                if decision.lower() == 'y':
                    print(f"meaning -",jmespath.search("".join(close_match),load_file))
            else:
                print("word not present in the dictionary")
    
            

