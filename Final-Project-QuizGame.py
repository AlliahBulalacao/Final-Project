import random
from itertools import repeat

num_repeat = 10

answer = input("Play game? ('Y' to continue) ")


while True:
    if answer == "Y":

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

    items = int(input('How many items would you like to answer? '))

    dict_list = list(vocab_antonyms.keys())

    random.shuffle(dict_list)
    correct = 0
    wrong = 0

    for keyword in dict_list:
        for i in range(0, items):
            display = "{}"

            print(display.format(keyword))
            ans = input("Answer for Antonyms: ")
            print(vocab_antonyms[keyword])

            if ans == vocab_antonyms[keyword]:
                print("Your answer is correct\n")
                correct += 1

            else:
                print("Your answer is wrong\n")
                wrong += 1
        break
    repeat = input('Would you like to continue? ')
    if repeat == 'Y':
        continue
    elif repeat == 'N':
        break
    break

