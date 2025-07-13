import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
from nltk.probability import FreqDist

# sample documents
documents = [
    "The quick brown fox jumps over the lazy dog.",
    "The dog barks loudly, and the fox runs away.",
    "A quick brown cat chases a mouse.",
]

# original documents
for i, statement in enumerate(documents):
    print(f"Doc {i} - {statement}")

stop_words = list(set(stopwords.words("english")))
processed_tokens = []

for doc in documents:
    # lower the statement
    doc = doc.lower()

    # get all tokens
    tokens = word_tokenize(doc)

    # remove all punctuations
    tokens = [token for token in tokens if token.isalpha()]

    # remove stop words
    tokens = [token for token in tokens if token not in stop_words]
    # print(tokens)

    processed_tokens.append(tokens)

# get all token in one list
all_token = [token for sublist in processed_tokens for token in sublist]

# get unique list
all_token_unique_list = sorted(list(set(all_token)))
# print(all_token_unique_list)
# print(all_token_unique_list)

# convert all token from list to dictionary

# token_dict = {token: 0 for token in all_token_unique_list}
# print(token_dict)
bow_vectors = []

for doc in processed_tokens:
    # print(doc)
    fdist = FreqDist(doc)
    # print(fdist['chases'])
    # for key, item in fdist.items():
    #     print(key + "->" + str(item))
    
    vector = [fdist[word] for word in all_token_unique_list]
    bow_vectors.append(vector)
    
print(bow_vectors)

bow_df = pd.DataFrame(bow_vectors, columns=all_token_unique_list, index=[f'Doc {i+1}' for i in range(len(documents))])
print(bow_df)


# count vectorize
