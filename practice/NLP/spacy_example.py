import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("i left thexite room")
for word in doc:
    print(
        word.text
        + " -> "
        + word.pos_
        + " -> "
        + word.tag_
        + " -> "
        + spacy.explain(word.tag_)
    )
