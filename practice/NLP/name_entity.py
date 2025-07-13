from nltk import ne_chunk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

NE_sent = "apple The US President stays in the white house"

NE_tags = pos_tag(word_tokenize(NE_sent))
print(ne_chunk(NE_tags))

