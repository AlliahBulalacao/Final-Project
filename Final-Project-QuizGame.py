# Guess the antonym of the words
# Must type in answer exactly as it appears in the Dictionary

import random

answer = input("Play game? ('Y' to continue) ")
print(" ")
while answer == "Y":

    vocab_antonyms = { "artificial": "natural", "arrive": "depart", "argue": "agree", "all": "none",
        "amateur": "professional", "alive": "dead","advanced": "elementary",
        "adult": "child", "ancestor": "descendant","boy": "girl",
        "build": "destroy", "borrow": "lend", "body": "soul", "blunt": "sharp",
        "boring": "exciting", "cold": "hot", "careful": "careless",
        "dainty": "clumsy", "callous": "sensitive", "desperate": "hopeful",
        "exit": "entrance", "forbid": "allow", "future": "past", "gentle": "violent",
        "gaiety": "misery", "giant": "tiny", "evening": "morning",
        "exclude": "include", "hopeful": "desperate", "harvest": "plant",
        "intelligent": "silly", "interrupt": "continue", "insult": "compliment",
        "loser": "winner", "negative": "affirmative", "narrow": "broad",
        "humble": "proud", "important": "trivial", "permanent": "temporary",
        "guilty": "innocent", "external": "internal", "expand": "compress",
        "brighten": "fade", "happy": "sad", "melt": "freeze"}

    dict_list = list(vocab_antonyms.keys())

    random.shuffle(dict_list)


