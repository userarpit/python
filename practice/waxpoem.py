import random

nouns = [
    "fossil",
    "horse",
    "aardvark",
    "judge",
    "chef",
    "mango",
    "extrovert",
    "gorilla",
]

verbs = [
    "kicks",
    "jingles",
    "bounces",
    "slurps",
    "meows",
    "explodes",
    "curdles",
]

adjectives = [
    "furry",
    "balding",
    "incredulous",
    "fragrant",
    "exuberant",
    "glistening",
]

prepositions = [
    "against",
    "after",
    "into",
    "beneath",
    "upon",
    "for",
    "in",
    "like",
    "over",
    "within",
]

adverbs = [
    "curiously",
    "extravagantly",
    "tantalizingly",
    "furiously",
    "sensuously",
]

three_nouns = random.sample(nouns, k=3)

three_verbs = random.sample(verbs, k=3)
three_adjectives = random.sample(adjectives, k=3)
two_prepositions = random.sample(prepositions, k=2)
one_adverb = random.choice(adverbs)

vowel = ["a", "e", "i", "o", "u"]

article = ["An" if three_adjectives[0][0] in vowel else "A"]

print(f"{article[0]} {three_adjectives[0]} {three_nouns[0]}")

print(
    f"\n{article[0]} {three_adjectives[0]} {three_nouns[0]} {three_verbs[0]} \
{two_prepositions[0]} the {three_adjectives[1]} {three_nouns[1]}"
)

print(f"{one_adverb}, the {three_nouns[0]} {three_verbs[1]}")
print(
    f"the {three_nouns[1]} {three_verbs[2]} {two_prepositions[1]} a \
{three_adjectives[2]} {three_nouns[2]}"
)
